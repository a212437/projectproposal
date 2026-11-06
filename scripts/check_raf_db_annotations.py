#!/usr/bin/env python3
"""Validate RAF-DB basic-subset annotation files and print age/emotion counts."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

AGE_BINS = {0: "0-3", 1: "4-19", 2: "20-39", 3: "40-69", 4: "70+"}
EMOTIONS = {
    1: "Surprise",
    2: "Fear",
    3: "Disgust",
    4: "Happiness",
    5: "Sadness",
    6: "Anger",
    7: "Neutral",
}


def read_labels(path: Path) -> dict[str, int]:
    labels: dict[str, int] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            line = raw.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(
                    f"{path}:{line_number}: expected 2 columns, got {len(parts)}"
                )
            name, value = parts
            labels[name] = int(value)
    return labels


def split_of(name: str) -> str:
    return name.split("_", 1)[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raf_root", type=Path, help="Path to the raf-basic folder")
    args = parser.parse_args()

    emo_path = args.raf_root / "EmoLabel" / "list_patition_label.txt"
    age_path = args.raf_root / "AgeLabel" / "list_patition_label.txt"

    emotion = read_labels(emo_path)
    age = read_labels(age_path)

    if set(emotion) != set(age):
        missing_age = sorted(set(emotion) - set(age))
        missing_emotion = sorted(set(age) - set(emotion))
        raise SystemExit(
            "Image names differ between the two files: "
            f"{len(missing_age)} missing from age labels, "
            f"{len(missing_emotion)} missing from emotion labels"
        )

    invalid_age = sorted({value for value in age.values() if value not in AGE_BINS})
    invalid_emotion = sorted(
        {value for value in emotion.values() if value not in EMOTIONS}
    )
    if invalid_age:
        raise SystemExit(f"Unexpected age labels: {invalid_age}")
    if invalid_emotion:
        raise SystemExit(f"Unexpected emotion labels: {invalid_emotion}")

    train_count = sum(split_of(name) == "train" for name in age)
    test_count = sum(split_of(name) == "test" for name in age)

    print(f"Images: {len(age)}")
    print(f"Train: {train_count}")
    print(f"Test:  {test_count}")
    print()

    print("Age bins")
    print(
        f"{'label':>5}  {'range':<6}  {'train':>6}  {'test':>6}  "
        f"{'total':>6}  {'share':>7}"
    )
    for label, name in AGE_BINS.items():
        counts = Counter(
            split_of(image) for image, value in age.items() if value == label
        )
        total = counts["train"] + counts["test"]
        share = 100 * total / len(age)
        print(
            f"{label:>5}  {name:<6}  {counts['train']:>6}  "
            f"{counts['test']:>6}  {total:>6}  {share:>6.2f}%"
        )

    print()
    print("Emotion classes")
    for label, name in EMOTIONS.items():
        total = sum(value == label for value in emotion.values())
        print(f"{label} {name:<10} {total:>6}")

    print()
    print("Age x emotion")
    cross: dict[tuple[int, int], int] = defaultdict(int)
    for image, age_label in age.items():
        cross[(age_label, emotion[image])] += 1
    print("age  emotion      count")
    for age_label in sorted(AGE_BINS):
        for emotion_label in sorted(EMOTIONS):
            count = cross.get((age_label, emotion_label), 0)
            print(f"{age_label:>3}  {EMOTIONS[emotion_label]:<10}  {count:>6}")


if __name__ == "__main__":
    main()
