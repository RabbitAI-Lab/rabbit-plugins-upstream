## Description:

罚款与违约金台账逐项核对（余额复算、合计勾稽、单号重复、空缺与占位符、方向与金额符号、日期倒挂），每条结论都引用原文行号，第三方可用同一份输入复算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and operations users use this skill to check penalty and liquidated-damages ledgers before monthly close or annual settlement. It recomputes balances, checks totals, detects repeated document numbers, flags missing fields and placeholders, checks direction/sign consistency, and reports date-order issues with source line references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade path asks an agent to run an unpinned remote installer and begin a purchase or installation flow.

Mitigation: Review the SkillPay/Alipay source and exact package version before running installer commands, and require the user to personally confirm wallet authorization, payment, or new skill installation.

Risk: The checker reads local ledger input that may contain sensitive finance or counterparty information.

Mitigation: Run it only in a trusted local environment and provide only ledger data the user is comfortable processing with a local Node script.

Risk: The free version omits six checks and does not provide tax or legal advice.

Mitigation: Present the executed and omitted checks clearly, avoid treating a clean result as a tax/legal conclusion, and seek professional review for tax deductibility or legal determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/penalty-settlement-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade public entry](https://skillpay.alipay.com/public/tokendidi)
- [Upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay installation guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON containing ledger findings, summary totals, executed checks, omitted checks, scope notes, and source-line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a text ledger with recognizable headers; insufficient input returns missing requirements instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
