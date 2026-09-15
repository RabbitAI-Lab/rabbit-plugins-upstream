## Description:

增值税申报与账载开票对照表逐项核对，每条结论都带原文依据，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping users use this skill during monthly close, reconciliation, or review to compare VAT filing, book income, and invoice-system figures. It performs the free local checks for row arithmetic, totals, duplicate periods, and missing or placeholder fields, with source-cited findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free local VAT reconciliation tool is offline, but the skill text also points users toward an external paid upgrade flow that installs unpinned remote code and follows another skill's instructions.

Mitigation: Treat the paid upgrade flow as outside this reviewed skill; require explicit user confirmation before any network install, wallet action, payment, or newly installed skill instructions are followed.

Risk: The skill produces Chinese-language financial reconciliation output and may be unsuitable for users who cannot review that output accurately.

Mitigation: Install and use it only when the operator can understand the Chinese prompts, findings, and limitations.

Risk: The tool checks arithmetic and consistency across VAT filing, books, and invoices, but does not determine whether tax treatment or tax rates are legally correct.

Mitigation: Use findings as reconciliation evidence and seek qualified tax review for tax-law applicability, filings, corrections, or disputes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-filing-reconcile-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional complete-edition shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable Chinese text or JSON findings from a local Node.js script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite input rows and distinguish executed free checks from checks not included in this edition.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
