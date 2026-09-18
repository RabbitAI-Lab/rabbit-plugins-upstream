## Description:

发票领用存台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashier teams use this skill during monthly close, reconciliation, or inventory checks to verify invoice usage and stock ledgers. It checks row arithmetic, total reconciliation, duplicates, blanks, and placeholder values while citing source lines for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes an upgrade path that asks users to send a purchase/install prompt to an AI assistant and run payment-related installer automation outside the core invoice checking purpose.

Mitigation: Use the free local checks without the upgrade automation unless the package, merchant, product, and payment flow have been independently verified through a trusted channel.

Risk: The free version intentionally omits cross-month continuity, abnormal void-rate, abnormal reversal-rate, non-integer count, and no-receipt-but-issued checks.

Mitigation: Treat results as limited to the listed free checks and review `checks_not_run` before relying on the output for a complete ledger review.

Risk: The tool checks invoice usage and stock ledger arithmetic, not tax compliance or the legal validity of voids and reversals.

Mitigation: Route tax compliance questions and disputed void or reversal treatment to qualified reviewers or a separate tax-compliance workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/invoice-usage-stock-check-free)
- [Optional paid-version purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON with invoice-ledger findings, executed checks, withheld checks, and status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers when checks run; insufficient input returns missing fields instead of a ledger conclusion.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
