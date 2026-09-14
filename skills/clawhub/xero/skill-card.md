## Description:

Xero API integration with managed OAuth for managing contacts, invoices, payments, accounts, bank transactions, and financial reports through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to read, report on, and, with explicit approval, modify Xero accounting records through a Maton-authenticated connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Xero accounting data through a Maton/Xero connection.

Mitigation: Install only when that access is acceptable, use OAuth where possible, choose the narrowest Xero scopes and exact connection, and remove unused connections.

Risk: Write operations, new connections, hosted functions, triggers, and invocations can change business data or automate future actions.

Mitigation: Require separate user approval for each write, connection, hosted function, trigger, destination, or invocation after showing the target, payload, connection, and intended effect.

Risk: Persistent trigger destinations can continuously forward event data to external URLs.

Mitigation: Prefer Maton-controlled destinations, avoid third-party trigger destinations unless the user controls the host and understands what will be forwarded, and delete unused triggers and destinations.

Risk: Long-lived API keys and local event handlers increase credential and execution risk.

Mitigation: Prefer OAuth over API keys, avoid exposing MATON_API_KEY, use dedicated Maton accounts for hosted functions, and run only user-authored or user-reviewed handlers.

## Reference(s):

- [Xero API Overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Accounts API](https://developer.xero.com/documentation/api/accounting/accounts)
- [Xero Payments API](https://developer.xero.com/documentation/api/accounting/payments)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Xero API endpoint paths, Maton CLI commands, JSON payloads, OAuth and connection instructions, and approval checkpoints.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
