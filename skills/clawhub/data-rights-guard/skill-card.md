## Description:

Helps assess dataset licenses, commercial-use rights, attribution, and source traceability before data enters AI training or evaluation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and data stewards use this skill to flag missing licenses, noncommercial restrictions, attribution gaps, and untraceable sources before using data for training, fine-tuning, or evaluation. Findings support human review rather than legal clearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local rights check can miss license conditions or be mistaken for legal approval to train on data.

Mitigation: Review the original license and provenance with a qualified human before including data in a training set; do not treat a pass as legal advice.

Risk: The code and documentation have different reuse terms, and the instructions are primarily in Chinese.

Mitigation: Read the packaged license scope before reuse and have a reviewer who can understand the instructions confirm any consequential interpretation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/data-rights-guard)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Chinese-language plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-item status and issues, excluded-item count, and suggested follow-up; not automatic legal approval.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
