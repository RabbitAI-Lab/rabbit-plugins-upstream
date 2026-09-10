## Description:

QuickBooks provides managed OAuth access to QuickBooks Online through Maton for retrieving and administering customers, vendors, invoices, payments, and financial reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to perform QuickBooks Online accounting administration through Maton, including listing records, retrieving reports, and creating or updating business records when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real financial changes in QuickBooks.

Mitigation: Use a least-privileged QuickBooks account and approve write operations only after checking the endpoint, resource ID, amount, and accounting consequence.

Risk: Long-lived API keys can be exposed more easily than OAuth-managed credentials.

Mitigation: Prefer OAuth over API keys and avoid installing the skill where QuickBooks administration is not needed.

Risk: Ambiguous Maton connections can send requests to the wrong QuickBooks account.

Mitigation: Specify the intended Maton connection before calls, especially before any operation that changes accounting records.

Risk: The Maton CLI or SDK package source could be substituted or untrusted.

Mitigation: Consider pinning or verifying the Maton CLI or SDK package source before installation.

## Reference(s):

- [ClawHub QuickBooks Skill](https://clawhub.ai/byungkyu/skills/quickbooks)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [QuickBooks API Overview](https://developer.intuit.com/app/developer/qbo/docs/get-started)
- [QuickBooks Customers API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer)
- [QuickBooks Invoices API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice)
- [QuickBooks Payments API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment)
- [QuickBooks Profit and Loss Reports API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/profitandloss)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose QuickBooks API calls through Maton; write operations require explicit user approval.]

## Skill Version(s):

1.2.1 (source: server release metadata; frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
