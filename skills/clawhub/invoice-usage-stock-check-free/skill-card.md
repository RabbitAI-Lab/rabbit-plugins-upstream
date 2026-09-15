## Description:

发票领用存台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashiering teams use this skill during monthly close, reconciliation, and inventory checks to validate invoice usage and stock ledgers. It recalculates row-level stock formulas, checks totals, detects duplicate months and blank placeholders, and reports findings with source line references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional upgrade instructions direct users toward an unpinned remote installer and a purchase/install flow for separate follow-on software.

Mitigation: Do not run the optional full-version upgrade command unless the package source, exact version, payment flow, and newly installed skills are independently verified.

Risk: Invoice ledger inputs may contain sensitive business or tax records.

Mitigation: Use the free checker only with local files the user intentionally provides, and keep the workflow local.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/invoice-usage-stock-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf for optional full version](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation and purchase guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON findings with status, scope, finding details, summary, and omitted checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided ledger text; insufficient input returns missing requirements rather than a positive or negative conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
