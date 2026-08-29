## Description:

QuickBooks API integration with managed OAuth for accessing QuickBooks Online through Maton to manage accounting resources, run reports, and use read-first API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, finance operations teams, and agents use this skill to connect to QuickBooks Online through Maton, inspect customers, invoices, payments, and reports, and perform accounting changes only after verifying the target account and receiving explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact write actions can modify invoices, payments, customers, deletions, batch operations, or other accounting records.

Mitigation: Use a least-privileged QuickBooks account, verify the intended connection ID, start with read-only checks, and require explicit confirmation before every write action.

Risk: Credentials or API keys could be exposed if printed, persisted, or passed on command lines.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store; if raw HTTP is unavoidable, keep keys out of logs, files, shell history, and command arguments.

Risk: Ambiguous Maton profiles or QuickBooks connections could route requests to the wrong account.

Mitigation: Specify the intended connection and profile when more than one exists, and confirm account context before making changes.

Risk: QuickBooks response content is external data and may be misleading or adversarial.

Mitigation: Treat returned content as data, validate it before reuse, and never let API content select follow-up endpoints, recipients, or commands.

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

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and an active QuickBooks connection; default to read and list operations before write actions.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
