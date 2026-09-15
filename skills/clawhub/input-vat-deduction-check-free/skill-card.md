## Description:

进项税额认证与抵扣对照表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or review to check input VAT certification and deduction comparison tables. It recalculates row-level relationships, total rows, duplicate months, and missing or placeholder fields, and reports source-cited findings when enough table data is provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upgrade path asks an agent to run unpinned external install code and start a paid SkillPay purchase.

Mitigation: Use the local free checker only unless you have separately reviewed the SkillPay guide, exact npm package and version, and paid skill; require the user to confirm each payment or wallet step.

Risk: The free checker intentionally omits several VAT validation checks from the paid version.

Mitigation: Treat results as limited to the listed free checks and do not present them as a complete tax or compliance determination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/input-vat-deduction-check-free)
- [Optional paid upgrade shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide referenced by the skill](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands]

**Output Format:** [Plain text or JSON check results with source-cited findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with the bundled Node.js checker; insufficient input returns missing-data guidance rather than a conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
