## Description:

平台结算单逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users can run local checks on ecommerce platform settlement statements during monthly closing, reconciliation, or inventory review. The skill helps identify arithmetic mismatches, incorrect totals, duplicate order IDs, blank fields, and parseable amount issues with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled checker is local, but the documentation includes an optional paid-upgrade workflow that points an agent toward an unpinned external install and purchase process.

Mitigation: Use the free local checker unless the package, publisher, version, permissions, and payment flow have been independently verified; do not allow an agent to initiate purchases or run unpinned install commands without explicit user confirmation.

Risk: The free checker covers arithmetic, total-row, duplicate-order, blank-field, and amount-parsing checks, but does not verify bank payouts, platform fee fairness, logistics truth, returns truth, tax treatment, or audit opinions.

Mitigation: Treat outputs as settlement-table reconciliation signals and separately review excluded business, payment, logistics, tax, and audit questions with the appropriate records or experts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/platform-settlement-check-free)
- [SkillPay storefront referenced by artifact documentation](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation and purchase guide referenced by artifact documentation](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON settlement-check results with findings, source line numbers, summaries, and remediation advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; returns insufficient-input status rather than conclusions when required settlement-table evidence is missing.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
