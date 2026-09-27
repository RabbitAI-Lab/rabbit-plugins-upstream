## Description:

QuickBooks API integration with managed OAuth for accounting administration through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to guide agents through authenticated QuickBooks Online administration, including customer, vendor, invoice, payment, and financial report workflows. It is intended for tasks where the user can review connection choices and approve writes before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact QuickBooks accounting actions that mutate business records.

Mitigation: Default to read and list operations, require explicit user approval for every write, and verify the endpoint, account, resource ID, amount, and consequence before execution.

Risk: Using the wrong QuickBooks connection can expose or modify the wrong company's accounting data.

Mitigation: Use a least-privileged QuickBooks account, verify the intended connection ID before each request, and delete unused connections.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, keep the key out of logs, shell history, files, and command arguments, and rotate it if exposed.

Risk: Hosted functions, triggers, or destinations can continue operating after the initial task.

Mitigation: Approve automation explicitly, keep network access and connected accounts least-privileged, and delete unused functions, triggers, or destinations.

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
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, HTTP examples, JSON snippets, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide agent behavior and do not directly execute QuickBooks actions without user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
