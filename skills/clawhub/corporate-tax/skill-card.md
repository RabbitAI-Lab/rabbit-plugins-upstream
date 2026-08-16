## Description:

Corporate Tax is a Chinese-language corporate finance and tax skill suite for voucher generation, internal audit, VAT management, month-end close, annual tax settlement, financial analysis, financial statements, and budget analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax employees use this skill to route requests to structured templates for accounting vouchers, tax calculations, financial reporting, budget analysis, and audit-oriented review. It supports CAS-oriented checks and structured deliverables that still require qualified finance or tax review before filing, reporting, or audit use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle sensitive corporate finance, tax, and audit records.

Mitigation: Redact unnecessary personal or confidential fields before use and limit shared inputs to the minimum needed for the requested workflow.

Risk: The security summary reports that outputs can be persisted to Notion without clear per-write consent or destination controls.

Mitigation: Before using Notion, confirm the exact workspace, page, or database destination and obtain explicit approval for each write.

Risk: Generated tax, accounting, reporting, or audit outputs may be incomplete or unsuitable for formal filing or audit reliance.

Mitigation: Have a qualified finance, tax, or audit reviewer validate outputs before filing, reporting, or audit use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ebandao777-oss/skills/corporate-tax)
- [Server-Resolved GitHub Provenance](https://github.com/ebandao777-oss/corporate-tax)
- [Corporate Tax README](artifact/README.md)
- [Journal Entries Reference](artifact/references/journal-entries.md)
- [Internal Audit Reference](artifact/references/internal-audit.md)
- [VAT Management Reference](artifact/references/vat-management.md)
- [Month-End Closing Reference](artifact/references/month-end-closing.md)
- [Annual Tax Settlement Reference](artifact/references/annual-tax-settlement.md)
- [Financial Analysis Reference](artifact/references/financial-analysis.md)
- [Financial Statements Reference](artifact/references/financial-statements.md)
- [Budget Analysis Reference](artifact/references/budget-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with structured tables, checklists, calculations, and optional file-oriented deliverables when requested by a template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include finance, tax, audit, and reporting guidance that should be reviewed by qualified personnel before operational use.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
