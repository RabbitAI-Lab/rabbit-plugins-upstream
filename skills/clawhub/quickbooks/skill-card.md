## Description:

QuickBooks API integration with managed OAuth for administering QuickBooks Online customers, vendors, invoices, payments, reports, and approved Maton-hosted automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help an agent administer QuickBooks Online through Maton-managed OAuth, including reading accounting records, preparing approved changes, and setting up explicitly approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QuickBooks actions can affect accounting records such as invoices, payments, bills, customers, and vendors.

Mitigation: Default to read and list calls, verify the target connection and resource IDs, and require explicit approval with a financial-impact summary before any write action.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding event data after setup.

Mitigation: Require separate approval for each function, trigger, or destination, use user-reviewed handlers, prefer least-privileged connections, and remove automations when the task is complete.

Risk: Long-lived credentials or broad QuickBooks authorizations can increase exposure if used casually.

Mitigation: Prefer OAuth, use the least-privileged QuickBooks account and scopes available, avoid exported API keys when possible, and revoke unused connections promptly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/quickbooks)
- [Maton Homepage](https://maton.ai)
- [QuickBooks API Overview](https://developer.intuit.com/app/developer/qbo/docs/get-started)
- [QuickBooks Customers API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer)
- [QuickBooks Invoices API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice)
- [QuickBooks Payments API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment)
- [QuickBooks Profit and Loss Reports API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/profitandloss)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated QuickBooks API calls and approved automation setup through Maton.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence; artifact metadata reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
