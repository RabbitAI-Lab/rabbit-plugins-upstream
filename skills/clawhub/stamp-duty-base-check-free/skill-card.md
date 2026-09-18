## Description:

印花税计税依据台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and compliance users can use this skill during monthly or quarterly reconciliation to check stamp-duty tax-basis ledgers for arithmetic mismatches, total-row inconsistencies, duplicate contract numbers, and missing required fields. The skill runs locally over user-provided ledger text or JSON input and withholds conclusions when required material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an unpinned external installer, paid purchase flow, and instructions from a newly installed unaudited skill.

Mitigation: Use the free local checker independently unless the user separately verifies the package and version, merchant and product identifiers, official payment links, and any newly installed skill before following upgrade instructions.

Risk: The checker is scoped to the free checks and does not perform withheld or out-of-scope tax judgments.

Mitigation: Treat the output as ledger reconciliation support, review the omitted checks, and consult appropriate tax expertise for taxability, rate selection, exemptions, or special cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/stamp-duty-base-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Complete edition purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable terminal text or JSON results with findings, scope, summary, omitted checks, and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled runner returns exit codes for success, missing input, insufficient material, parse failures, and unexpected errors.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
