## Description:

坏账准备计提表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and audit-support users use this skill during month-end closing, reconciliation, or inventory-style review to check bad-debt provision tables. It recomputes row-level provision amounts, checks totals, flags duplicates or missing fields, and withholds conclusions when required table evidence is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free checker as a complete bad-debt provision review even though several checks are explicitly outside this release.

Mitigation: Review the listed checks_not_run and use the output as support for the included arithmetic, total, duplicate, and missing-field checks only.

Risk: Accounting inputs may contain sensitive receivables data.

Mitigation: Run the packaged local checker as intended; evidence.security reports no hidden network, persistence, or credential behavior.

Risk: Missing or unrecognized required headers can produce no substantive conclusion.

Mitigation: Provide copied table text with customer, aging bucket, receivable balance, provision rate, and provision amount columns, and treat insufficient_input as no check performed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bad-debt-provision-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text or JSON findings from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when checks run; insufficient input returns missing-field guidance instead of a clean result.]

## Skill Version(s):

1.0.59 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
