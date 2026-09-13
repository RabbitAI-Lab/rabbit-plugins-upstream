## Description:

Zoho Books API integration with managed OAuth for reading and managing invoices, contacts, bills, expenses, and other accounting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect and manage Zoho Books accounting records through Maton-managed OAuth. It supports read, create, update, and delete workflows for invoices, contacts, bills, expenses, sales orders, purchase orders, and related financial data when the user has approved the connection and operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete financial records in Zoho Books.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user confirmation of the target resource, payload, and intended effect before any write or delete.

Risk: Maton API keys or OAuth-derived credentials could be exposed if printed, logged, persisted, or passed through shell history.

Mitigation: Prefer OAuth through the Maton CLI, never inspect credential stores or print secrets, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Hosted functions and triggers can automate access to business data and create persistent data flows.

Mitigation: Use user-authored or user-reviewed handlers, deploy with DENY_ALL network policy unless a host-specific exception is approved, and keep trigger destinations on Maton-controlled endpoints unless the user explicitly approves a third-party host and data flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-books)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Books API v3 Introduction](https://www.zoho.com/books/api/v3/introduction/)
- [Zoho Books Invoices API](https://www.zoho.com/books/api/v3/invoices/)
- [Zoho Books Contacts API](https://www.zoho.com/books/api/v3/contacts/)
- [Zoho Books Bills API](https://www.zoho.com/books/api/v3/bills/)
- [Zoho Books Expenses API](https://www.zoho.com/books/api/v3/expenses/)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated Maton CLI commands, raw HTTP examples, hosted-function snippets, trigger setup guidance, and concise summaries of Zoho Books API responses.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter metadata version: 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
