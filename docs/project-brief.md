# Project Brief

**Student:** Joshua A/L Murugan (A212437)
**Supervisor:** Dr. Kok Ven Jyn (vj.kok@ukm.edu.my)
**Programme:** Intelligent Machine (Computer Science)

This document confirms the final topic, objectives and methodology and explains how RAF-DB and CAFE will be used.

## 1. Final topic

**Benchmarking and Parameter-Efficient Fine-Tuning (PEFT) of Adult Facial Expression Recognition (FER) Models on Child Expressions (Topic 2).** The project measures how well FER models trained on adult faces transfer to children aged 2 to 8 and whether LoRA and an age-aware adapter close the gap at low cost. It uses static images and seven emotion classes. It does not cover infants, spontaneous expressions, video or clinical use.

## 2. Research questions

- **RQ1.** To what extent do adult-trained ResNet-50 and ViT-B/16 models degrade on child facial expressions in CAFE, and which emotion classes are most affected?
- **RQ2.** How does LoRA compare with full fine-tuning and linear probing in child FER accuracy, minority-class recall and parameter efficiency under full-data and low-data regimes?
- **RQ3.** Can an age-aware adapter with a class-conditional domain-adversarial loss improve child expression recognition and reduce age-related feature entanglement without degrading adult performance?

## 3. Objectives

1. Build a reproducible RAF-DB-to-CAFE benchmark with subject-disjoint CAFE splits and evaluate ResNet-50 and ViT-B/16 without adaptation and after adaptation. This covers the topic's first objective and RQ1.
2. Implement and compare linear probing, LoRA (HuggingFace PEFT) and full fine-tuning, reporting accuracy, macro-F1, per-class recall, calibration, trainable parameters, memory and training time. This covers the topic's first objective and RQ2.
3. Design and evaluate an age-aware adapter with a domain-adversarial loss checked with an age probe, a dataset-identity probe and attention maps. The domain-adversarial option was chosen instead of meta-learning and covers RQ3.

## 4. Methodology

- **Source training.** Train ResNet-50 and ViT-B/16 (ImageNet-initialised) on the adult part of RAF-DB.
- **Source-only test.** Evaluate those models directly on CAFE. This is the baseline that answers RQ1.
- **Adaptation on CAFE.** Compare linear probing, LoRA (ranks 4, 8, 16) and full fine-tuning.
- **Low-data regimes.** Repeat with 1, 5, 10 and 20 labelled images per class.
- **Age-aware adapter.** Add a bottleneck adapter with a gradient-reversal domain classifier, in a class-conditional form. Two variants: adult-vs-child labels and CAFE age bins (2–4, 5–6, 7–8) so that dataset differences do not stand in for age.
- **Evaluation.** Accuracy, macro-F1, unweighted average recall, per-class recall (fear, sadness, surprise), calibration error, parameter percentage, memory and training time.
- **Statistics.** Five subject-disjoint folds, three seeds and confidence intervals that resample children, not images.
- **Reproducibility.** Private GitHub repository, W&B run tracking, fixed seeds, logged split files and a 6 GB NVIDIA RTX 4050 GPU.

## 5. How the two datasets will be used

| | RAF-DB | CAFE |
|---|---|---|
| **Role** | Adult source for training the models | Child target for testing transfer and adaptation |
| **Content** | 15,339 basic-emotion images, 7 classes (12,271 train / 3,068 test) | 1,192 posed photographs of 154 children aged 2–8, 7 classes |
| **What I use** | Images aged 20+ only: 11,070 images (8,817 train / 2,253 test), selected with the age annotations; the ranges 0–3 and 4–19 are excluded | All images, split by child into 5 folds: 3 train, 1 validation, 1 test |
| **Used for** | Source training, validation, adult test (RQ3 check) | Source-only baseline (RQ1), linear probe, LoRA and full fine-tuning (RQ2), few-shot runs, adapter (RQ3) |
| **Limits** | In-the-wild, mixed ages, different capture conditions from CAFE; non-commercial research use only, with no redistribution or reproduction of its images or derived data | Small, posed, copyright-protected; labels are the expression each child was asked to pose; no images will be redistributed or shown in the report |

Both datasets are needed because the question is about the gap between adults and children. RAF-DB supplies the adult model and CAFE supplies the child test. Their capture conditions differ, so the result will be reported as a cross-age, cross-dataset benchmark and not as a pure age effect.

**Verification note (4 November 2026).** The RAF-DB age counts were checked against a public mirror of the official annotation files. The official release will still be used for the final experiments, and the counts will be re-checked once access is granted.

## 6. Dataset access I need

- **CAFE:** Access is through Databrary and needs authorisation by an authorised investigator, with students joining as affiliates. Status: application submitted; awaiting approval.
- **RAF-DB:** The owners require an e-mail application from a university account (name, affiliation, department, position, and a statement agreeing to the terms: non-commercial research use only, no sharing with third parties) before they send the password for the images and the annotation files that hold the age ranges. Status: not yet acquired.
- **If CAFE is delayed:** Build and test the pipeline on RAF-DB with approval at Week 8. The fallback is an age-stratified analysis inside RAF-DB (ages 0–19 versus adults), which has few images for some classes.

## 7. Timeline

| Week | Dates | Milestone |
|---|---|---|
| 6 | 2–8 Nov 2026 | D1 and D2 should be submitted; progress log and this brief; dataset access requested |
| 8 | 23–29 Nov 2026 | D3 requirements submitted; source-only baseline training; CAFE go or no-go |
| 10 | 7–13 Dec 2026 | D4 design submitted; LoRA vs full fine-tuning results |
| 12 | 21–27 Dec 2026 | D5 development submitted; age-aware adapter |
| 14 | 4–10 Jan 2027 | D6 final report submitted |
