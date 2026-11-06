# RAF-DB Age Summary

Basic-emotion subset: **15,339 images** (12,271 train / 3,068 test).

Source: RAF-DB `AgeLabel/list_patition_label.txt` and `EmoLabel/list_patition_label.txt`, checked from the public PrivateNet mirror. The official RAF-DB release will be used for the final experiments, and these counts will be re-checked once access is granted.

## Age bins

| Age label | Range | Train | Test | Total | Share |
|---|---|---:|---:|---:|---:|
| 0 | 0–3 | 1,283 | 329 | 1,612 | 10.51% |
| 1 | 4–19 | 2,171 | 486 | 2,657 | 17.32% |
| 2 | 20–39 | 6,531 | 1,662 | 8,193 | 53.41% |
| 3 | 40–69 | 1,920 | 502 | 2,422 | 15.79% |
| 4 | 70+ | 366 | 89 | 455 | 2.97% |
| **Total** | | **12,271** | **3,068** | **15,339** | **100.00%** |

## Adult and child/teen totals

| Group | Train | Test | Total | Share |
|---|---:|---:|---:|---:|
| 0–19 | 3,454 | 815 | 4,269 | 27.83% |
| 20+ | 8,817 | 2,253 | 11,070 | 72.17% |
| **Total** | **12,271** | **3,068** | **15,339** | **100.00%** |

## Notes

- Official age bins: 0–3, 4–19, 20–39, 40–69, 70+.
- The 4–19 bin is broad and includes older children and adolescents; it is not a clean child-only group.
- The 0–3 and 70+ bins are small and class-imbalanced, so per-class recall for fear, sadness and surprise should be reported.
- Do not commit the raw annotation files or images to the repository.
