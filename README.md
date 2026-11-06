# Adult-to-Child Facial Expression Recognition with PEFT

**Student:** Joshua A/L Murugan (A212437)
**Supervisor:** Dr. Kok Ven Jyn (vj.kok@ukm.edu.my)
**Programme:** Intelligent Machine (Computer Science)
**Status:** Week 6 — D1/D2 complete; repository pushed; CAFE application submitted; RAF-DB not yet acquired.
**Repository:** https://github.com/a212437/projectproposal
**Hardware:** NVIDIA RTX 4050, 6 GB VRAM
**Experiment tracking:** W&B project `project-proposal-topic2-adult-child-fer-peft`
**Last updated:** 4 November 2026

## Project summary

This project benchmarks how well adult-trained facial expression recognition (FER) models transfer to children aged 2–8, and whether parameter-efficient fine-tuning (PEFT) can narrow the gap at low computational and data cost. It uses RAF-DB as the adult source and CAFE as the child target, comparing ResNet-50 and ViT-B/16 under linear probing, LoRA and full fine-tuning. A second stage tests an age-aware adapter trained with a class-conditional domain-adversarial loss.

## Research questions

- **RQ1:** How much do adult-trained ResNet-50 and ViT-B/16 degrade on child expressions in CAFE, and which emotion classes are most affected?
- **RQ2:** How do linear probing, LoRA and full fine-tuning compare on child FER accuracy, minority-class recall and parameter efficiency under full-data and low-data regimes?
- **RQ3:** Can an age-aware adapter with a class-conditional domain-adversarial loss improve child recognition and reduce age-related feature entanglement without degrading adult performance?

## Repository layout

```text
FYP/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── project-brief.md
│   ├── progress-log.md
│   ├── raf-db-age-summary.md
│   └── proposal/
│       └── projectproposal.html
└── scripts/
    └── check_raf_db_annotations.py
```

The `src/`, `configs/`, `data/`, `checkpoints/` and `results/` folders will be added as the implementation develops.

## Current status

- D1 project plan and D2 literature review are written and validated.
- RAF-DB basic-subset annotation files have been checked: 15,339 images, 12,271 train and 3,068 test.
- Verified age counts: 0–3 = 1,612; 4–19 = 2,657; 20–39 = 8,193; 40–69 = 2,422; 70+ = 455.
- Adult 20+ subset: 11,070 images (8,817 train / 2,253 test).
- CAFE/Databrary application submitted and awaiting approval; official RAF-DB access not yet acquired.

## To complete before submission

- [ ] Make the GitHub repository private and invite the supervisor at `vj.kok@ukm.edu.my` as a collaborator.
- [ ] Create the W&B project `project-proposal-topic2-adult-child-fer-peft` and add its URL to `docs/progress-log.md`.
- [ ] Obtain official RAF-DB access (not yet acquired) and re-check the annotation counts against the official release.
- [ ] Record the CAFE/Databrary approval date and conditions when approved.
- [ ] Record installed package versions for reproducibility.

## Data policy

Do **not** commit RAF-DB or CAFE images, raw annotation files, model checkpoints or W&B run directories. Both datasets are for non-commercial research use and restrict redistribution. Keep data outside the repository in a local `data/` folder, which is ignored by Git. Commit only code, configuration, aggregate statistics, split specifications without image data, and documentation.

## Reproducibility

- Private GitHub repository with the supervisor added.
- Weights & Biases for run tracking: metrics, hyperparameters, seeds, checkpoints and system configuration.
- Fixed seeds and logged split files for every experiment.
- Every reported result should map to a W&B run and a Git commit.

## Next steps

1. Confirm CAFE/Databrary access and official RAF-DB access.
2. Build the RAF-DB data pipeline and subject-disjoint CAFE split specification.
3. Check LoRA support for ResNet-50 convolution layers in HuggingFace PEFT.
4. Create the W&B project and log the first baseline configuration.
5. Draft D3 requirements.

## Documentation

- [Project brief](docs/project-brief.md)
- [Progress log](docs/progress-log.md)
- [RAF-DB age summary](docs/raf-db-age-summary.md)
- [D1/D2 proposal](docs/proposal/projectproposal.html)
