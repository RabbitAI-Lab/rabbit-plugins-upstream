## Description:

加工贸易手册与保税料件核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Customs, document-control, and finance staff use this skill before monthly processing-trade close and manual cancellation to check a pasted bonded-material reconciliation table. It recomputes declared arithmetic, flags duplicates, blanks, placeholders, negative values, and total-row mismatches, and cites source rows for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on table-consistency findings as customs, legal, or tax advice.

Mitigation: Use the output as arithmetic and reconciliation assistance only; have customs, finance, or tax specialists confirm filing decisions and remediation.

Risk: The skill runs local Node.js code over business reconciliation data.

Mitigation: Run it only in a trusted workspace, inspect the bundled source before deployment, and avoid including unrelated secrets in input files.

Risk: Documentation mentions anonymous usage statistics, while security evidence found no confirmed network behavior.

Mitigation: Confirm the publisher's intended behavior before production rollout, and run in a network-restricted environment when data-handling policy requires it.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/toll-processing-manual-check-free)
- [Skill source manifest](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields rather than a conclusion.]

## Skill Version(s):

1.0.39 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
