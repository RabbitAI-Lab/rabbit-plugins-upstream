## Description:

增值税进销项汇总表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, accountants, and agents use this skill before Chinese VAT filing to check VAT input/output worksheets for arithmetic consistency, carryover credit issues, duplicate periods, blanks, and total-row mismatches. It returns findings with original line references and states when required worksheet material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free worksheet checks as a complete VAT or tax review.

Mitigation: Review the listed checks not run and out-of-scope items, especially output VAT from sales and rate, tax-burden range reasonableness, and negative-value cases.

Risk: Incomplete or malformed worksheet input can lead to no conclusion rather than a pass or fail result.

Mitigation: Provide a VAT input/output summary table with recognizable headers and review any missing-field response before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-burden-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console output or structured JSON findings with source line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and no conclusion.]

## Skill Version(s):

1.0.31 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
