## Description:

工时与人工成本分摊表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or inventory review to check labor cost allocation tables for row arithmetic, period totals, duplicate rows, blanks, and negative hours or rates. The free release reports only the listed checks and identifies missing input instead of producing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the checker as a full payroll, ERP, attendance, or legal review tool.

Mitigation: Use it only for the listed arithmetic and consistency checks, and route payroll policy, ERP, attendance, and legal questions to separate review.

Risk: The documentation contains inconsistent wording about no-network operation versus anonymous statistics.

Mitigation: Clarify the release documentation before deployment and rely on the security evidence that no actual network code was found in this version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/labor-cost-allocation-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Chinese-language terminal text or JSON result output, depending on the selected command option]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields and advice instead of a conclusion.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
