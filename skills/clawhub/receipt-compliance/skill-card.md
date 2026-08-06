## Description:

Accounting assistant for invoice OCR, invoice verification, reimbursement form filling, and approval-system handoff with enterprise-controlled configuration and local data processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Finance employees and accounting teams use this skill to extract invoice data, verify invoice details, generate reimbursement outputs, prepare approval submissions, classify expenses, flag invoice risk patterns, and assemble archive packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive financial data and may use optional remote verification, approval APIs, and archive outputs.

Mitigation: Decide which verification and approval connectors are allowed before use, avoid arbitrary custom endpoints unless controlled by the organization, and store outputs in restricted directories.

Risk: Local-only and no-storage claims can be misunderstood when optional remote connectors, caches, generated files, and archive packages are enabled.

Mitigation: Document which workflows remain local, which workflows contact approved services, and define retention and deletion rules for JSON, Excel, cache, and archive files.

Risk: OCR, invoice verification, and approval results can affect reimbursement or accounting decisions.

Mitigation: Require finance review of extracted fields, verification results, reimbursement forms, approval payloads, and risk reports before submission or posting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/receipt-compliance)
- [Enterprise setup guide](artifact/references/setup-guide.md)
- [Risk declaration](artifact/references/risk-declaration.md)
- [Tax rules](artifact/references/tax-rules.md)
- [Expense rules](artifact/references/expense_rules.md)
- [Account mapping](artifact/references/account_mapping.md)
- [Supplier scope rules](artifact/references/supplier_scope_rules.md)
- [Risk rules configuration](artifact/references/risk_rules_config.yaml)
- [API endpoints](artifact/references/api-endpoints.md)
- [China invoice verification portal](https://inv-veri.chinatax.gov.cn/)
- [DingTalk developer platform](https://open-dev.dingtalk.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, structured JSON, spreadsheet and voucher files, approval results, risk reports, and archive package outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require local OCR dependencies, enterprise connector configuration, restricted output directories, and retention rules for generated JSON, Excel, cache, and archive files.]

## Skill Version(s):

4.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
