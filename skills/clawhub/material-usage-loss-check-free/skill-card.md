## Description:

材料领用与损耗表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Finance, cashiering, project, and materials teams use this skill during monthly closing, reconciliation, or inventory checks to verify material usage and loss tables. It recalculates row arithmetic, checks totals, detects duplicates and blanks, and cites source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version is a limited arithmetic aid and does not perform several listed checks, including amount validation, reference loss-rate prompts, unit-consistency prompts, and negative-loss return-material detection.

Mitigation: Use the result as a focused table check, not a complete financial audit; manually review withheld checks or use a fuller review process before business decisions.

Risk: Documentation and scan guidance note potentially confusing wording about which checks are included.

Mitigation: Review the reported executed checks and withheld checks in the output before relying on any conclusion.

Risk: The skill is designed for Chinese-language material usage and loss tables and may not fit other document structures or accounting conventions.

Mitigation: Confirm that the input table has the expected headers and that local contract, construction, or accounting rules are reviewed separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/material-usage-loss-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON results, with Markdown instructions and inline shell commands in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.49 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
