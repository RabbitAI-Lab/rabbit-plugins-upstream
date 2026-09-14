## Description:

Data Rights Guard helps agents check training, fine-tuning, and evaluation data for license presence, commercial-use permission, attribution requirements, and source traceability before admitting it to a dataset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, data practitioners, and compliance reviewers use this skill to screen training, fine-tuning, or evaluation data before it enters an AI dataset. It supports repeatable checks for missing licenses, non-commercial restrictions, attribution gaps, and missing source traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rights-checking logic can incorrectly approve restricted data.

Mitigation: Treat the skill as advisory screening and manually review non-commercial, unknown, missing, and attribution-bearing licenses before data enters training.

Risk: Install instructions rely on mutable remote tooling.

Mitigation: Install only from a pinned, reviewed version or commit.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/data-rights-guard)
- [Project Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local CLI output; exit codes distinguish pass, findings, and usage errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
