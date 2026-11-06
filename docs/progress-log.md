# Progress Log

**Student:** [Student Name] ([Matric No.])
**Supervisor:** [Supervisor Name]
**Project:** Benchmarking and PEFT of Adult FER Models on Child Expressions
**Repository:** https://github.com/a212437/projectproposal
**Experiment tracking:** [W&B project URL]
**Last updated:** 4 November 2026

## Week 6 — 2–8 November 2026

### Work Completed This Week

- Wrote and validated the combined D1 project plan and D2 literature review, then checked each cited paper's claims against its abstract or full text.
- Verified the reference list and corrected metadata, author-name and scheduling issues in the D1/D2 document.
- Inspected the RAF-DB basic-emotion files: 12,271 training and 3,068 test images, with matching labels across 15,339 images.
- Downloaded the public RAF-DB annotation files from the PrivateNet repository and verified the age counts against the official basic-subset structure. The official release will still be used for the final experiments.
- Checked the CAFE dataset details against the original paper and its Databrary record.
- Wrote the project brief to finalise the topic, objectives, methodology and dataset use.
- Created the initial repository structure, README, requirements file, RAF-DB age summary and annotation-check script.
- Pushed the initial scaffold to https://github.com/a212437/projectproposal.

### Key Results & Interpretation

- RAF-DB basic-subset age counts (verified against the public annotation mirror): 0–3 = 1,612 (10.51%), 4–19 = 2,657 (17.32%), 20–39 = 8,193 (53.41%), 40–69 = 2,422 (15.79%) and 70+ = 455 (2.97%).
- About 28% of the subset is children or teenagers, so RAF-DB is not adult-only and must be filtered by age. The adult 20+ subset contains 11,070 images (8,817 train / 2,253 test), enough for source training.
- Prior work shows how large the gap can be. A small CNN trained on CK+ scored 93.55% on CK+ but only 46.5% on CAFE (Witherow et al., 2019). The source-only result in RQ1 is expected to be well below adult accuracy.
- No PEFT study found so far targets adult-to-child FER, which is the gap this project addresses.

### Problems/Issues

- CAFE access needs Databrary authorisation, which cannot be obtained without a supervisor or institutional route.
- Official RAF-DB access is still pending. The current annotation files are a public mirror, so the counts will be re-checked against the official release.
- RAF-DB and CAFE differ in capture conditions as well as age, so any drop in accuracy cannot be attributed to age alone. An age-bin adversary inside CAFE and a dataset-identity probe are planned to check this.
- Full fine-tuning of ViT-B/16 may be limited by GPU memory, so gradient accumulation and checkpointing are planned.

### Plan for Next Week (9–15 Nov 2026)

- Write the data pipeline and the subject-disjoint split specification, using RAF-DB only until CAFE access is confirmed.
- Check that HuggingFace PEFT supports LoRA on ResNet-50 convolution layers.
- Create the W&B project and log the first baseline configuration.
- Start drafting D3 (requirements).
- Make the GitHub repository private, add the supervisor, and create the W&B project.

## Template for Future Weeks

### Work Completed This Week

-

### Key Results & Interpretation

-

### Problems/Issues

-

### Plan for Next Week

-
