## Description:

Receipt Compliance helps agents OCR invoices, verify receipts, fill reimbursement forms, connect to approval systems, classify expenses, generate vouchers, reconcile bank statements, and prepare archive packages for finance workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Finance employees, operations teams, and developers use this skill to extract invoice data, check receipt authenticity, prepare reimbursement artifacts, and route approvals. It is a technical workflow aid and does not provide tax, accounting, or legal advice.

### Deployment Geography for Use:

Global, with China-focused invoice verification and tax-rule references.

## Known Risks and Mitigations:

Risk: The workflow reads and stores sensitive invoice, reimbursement, and bank-statement data.

Mitigation: Run it only in approved finance environments and store generated JSON, XLSX, CSV, ZIP, and log outputs in access-controlled locations.

Risk: Configured verification and approval integrations can send sensitive invoice or reimbursement data to external services despite local-only claims.

Mitigation: Approve allowed verification and approval services before use, disable integrations that are not approved, and document which data may leave the local environment.

Risk: Approval submissions may be difficult or impossible to revoke after they are sent to an enterprise approval platform.

Mitigation: Require human review of extracted fields, reimbursement amounts, recipients, and approval destinations before submission.

Risk: API keys and service credentials may be exposed if placed in files or shared logs.

Mitigation: Keep secrets in environment variables or a managed secret store, restrict file permissions, and rotate credentials on a defined schedule.

## Reference(s):

- [Enterprise Setup Guide](references/setup-guide.md)
- [Risk Declaration](references/risk-declaration.md)
- [Tax Rules](references/tax-rules.md)
- [API Endpoints](references/api-endpoints.md)
- [Expense Rules](references/expense_rules.md)
- [Account Mapping](references/account_mapping.md)
- [Supplier Scope Rules](references/supplier_scope_rules.md)
- [Risk Rules Configuration](references/risk_rules_config.yaml)
- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/receipt-compliance)
- [Publisher Profile](https://clawhub.ai/user/fyniujin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with command examples, structured JSON outputs, generated spreadsheet or archive files, and approval workflow configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent JSON, XLSX, CSV, ZIP, log, and approval-status artifacts containing sensitive finance data.]

## Skill Version(s):

4.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
