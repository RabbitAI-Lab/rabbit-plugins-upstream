## Description:

个税累计预扣计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance teams use this skill to check Chinese individual income tax cumulative withholding worksheets before payroll by recomputing rows, totals, duplicate personnel, and blank or placeholder fields. The free local checker requires source table text with headers and reports missing inputs instead of drawing conclusions from incomplete material.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The release security summary flags that the skill documentation steers users toward an unrelated external install and paid purchase workflow.

Mitigation: Use the free local checker only when that is the intended task; do not let an agent run the SkillPay or npx workflow, initiate purchases, or grant permissions without separately verifying the package, merchant, product, price, and consent.

Risk: The free checker executes only its declared subset of withholding checks and does not provide tax advice or conclusions when required table fields are missing.

Mitigation: Review omitted checks and missing-input reports before relying on results, and have payroll or tax professionals confirm issues that affect filings or payments.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/iit-withholding-check-free)
- [SkillPay shelf referenced by the skill documentation](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by the skill documentation](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided withholding table text; insufficient input returns missing fields instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
