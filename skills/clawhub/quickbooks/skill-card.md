## Description:

QuickBooks API integration with managed OAuth through the Maton CLI for accounting administration, including customers, vendors, invoices, payments, and financial reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users perform QuickBooks Online accounting administration through managed Maton authentication. It supports retrieving company and accounting data, managing customers, vendors, invoices, and payments, and running financial reports while treating write actions as high-impact financial operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QuickBooks write actions can change financial records such as customers, invoices, payments, and reports.

Mitigation: Default to read and list calls, retrieve the target resource first, and require explicit user approval after showing endpoint, resource IDs, amounts, and financial effect.

Risk: Requests can run against the wrong QuickBooks company or Maton account when multiple connections or profiles exist.

Mitigation: Verify the intended Maton connection before each request and specify the connection or profile when ambiguity exists.

Risk: Long-lived API keys and provider tokens can leak if printed, logged, written to files, or passed through shell commands.

Mitigation: Prefer OAuth, let the CLI or SDK credential store handle tokens, avoid exposing credential values, and use least-privileged accounts.

## Reference(s):

- [ClawHub QuickBooks Skill](https://clawhub.ai/byungkyu/skills/quickbooks)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [QuickBooks API Overview](https://developer.intuit.com/app/developer/qbo/docs/get-started)
- [QuickBooks Customers API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer)
- [QuickBooks Invoices API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice)
- [QuickBooks Payments API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment)
- [QuickBooks Profit and Loss Reports API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/profitandloss)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose QuickBooks API calls through the Maton CLI or SDK; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
