## Description:

Receipt Compliance helps accounting teams OCR invoices, verify authenticity, fill reimbursement forms, and connect configured approval systems with enterprise-controlled configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting teams use this skill to extract invoice data, prepare reimbursement records, generate accounting outputs, detect invoice-risk patterns, archive records, reconcile bank data, and submit configured approval workflows. The skill is intended for enterprise-controlled receipt and invoice processing, with human review for financial, tax, and external submission decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive financial records, including invoices and bank data.

Mitigation: Use a dedicated working directory, restrict local file permissions, and review generated records before sharing or importing them into enterprise systems.

Risk: Configured verification or approval features may send selected data to external tax-verification or approval platforms.

Mitigation: Review config.yaml before use, disable unused connectors, restrict API keys, and require manual confirmation before any external submission.

Risk: OCR, classification, tax, and reimbursement outputs may be incomplete or inaccurate.

Mitigation: Require finance or accounting review of extracted fields, tax treatment, risk warnings, and approval data before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/receipt-compliance)
- [Setup guide](references/setup-guide.md)
- [Risk declaration](references/risk-declaration.md)
- [Tax rules](references/tax-rules.md)
- [API endpoints](references/api-endpoints.md)
- [Account mapping](references/account_mapping.md)
- [Expense rules](references/expense_rules.md)
- [Supplier scope rules](references/supplier_scope_rules.md)
- [Risk rules configuration](references/risk_rules_config.yaml)
- [China tax invoice verification platform](https://inv-veri.chinatax.gov.cn/)
- [DingTalk Open Platform](https://open-dev.dingtalk.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, configuration examples, JSON examples, and generated local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured invoice JSON, reimbursement workbooks, approval payloads, risk reports, voucher import files, reconciliation reports, and archive packages when the corresponding scripts are run.]

## Skill Version(s):

4.2.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
