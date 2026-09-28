## Description:

Zoho Books API integration with managed OAuth for managing invoices, contacts, bills, expenses, and other accounting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to access Zoho Books through Maton-managed OAuth for approved accounting record reads and writes. It is intended for invoice, contact, bill, expense, order, credit note, and related Zoho Books workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Zoho Books accounting records and can perform writes or deletions when authorized.

Mitigation: Use OAuth, choose the narrowest Zoho scopes available, default to read/list operations, and confirm each write or deletion with the user before it runs.

Risk: Hosted functions, triggers, and destinations can keep acting automatically after setup.

Mitigation: Use them only when the user asks for hosted automation, require approval for each create/update/deploy/invocation, prefer DENY_ALL network policy for Zoho Books functions, and remove automations when they are no longer needed.

Risk: Long-lived API keys can be exposed if passed through environment variables or copied into raw HTTP workflows.

Mitigation: Prefer the documented OAuth flow and operating-system credential storage; use raw HTTP with MATON_API_KEY only where the CLI cannot be installed and avoid logging or persisting credentials.

## Reference(s):

- [Zoho Books API v3 Introduction](https://www.zoho.com/books/api/v3/introduction/)
- [Zoho Books Invoices API](https://www.zoho.com/books/api/v3/invoices/)
- [Zoho Books Contacts API](https://www.zoho.com/books/api/v3/contacts/)
- [Zoho Books Bills API](https://www.zoho.com/books/api/v3/bills/)
- [Zoho Books Expenses API](https://www.zoho.com/books/api/v3/expenses/)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for authenticated Zoho Books API use through Maton; write, delete, connection, function, and trigger actions require user confirmation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
