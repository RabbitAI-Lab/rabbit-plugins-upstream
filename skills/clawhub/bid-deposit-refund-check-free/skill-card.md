## Description:

保证金收退台账逐项核对，执行免费检查项并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and bid-operations users use this skill during month-end reconciliation, account checking, or inventory review to verify bid-deposit receipt and refund ledgers. It checks row arithmetic, totals, duplicate entries, missing fields, and refund/payment differences when sufficient ledger text is provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a paid-upgrade prompt that asks an assistant to install a remote payment package and start a purchase flow.

Mitigation: Use the free local checker only unless a human explicitly reviews and approves the SkillPay source, Alipay package, merchant product, and each payment step.

Risk: The security verdict is suspicious because remote installation and purchase actions could be initiated from documentation text.

Mitigation: Do not allow an agent to run the npx install command or initiate payment without separate human authorization and source verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bid-deposit-refund-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Alipay agent-payment build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON results with scope, findings, summary, and insufficient-input messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source line references when input is sufficient; insufficient input returns missing requirements and does not make a substantive conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
