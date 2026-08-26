## Description:

Zoho Books API integration with managed OAuth for reading and managing invoices, contacts, bills, expenses, and other accounting records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Zoho Books through Maton, inspect accounting data, and prepare or execute approved create, update, send, void, or delete operations on financial records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify financial records in Zoho Books.

Mitigation: Default to read and list calls, verify account context and identifiers first, and require explicit approval before create, update, send, void, or delete operations.

Risk: A new Zoho Books connection grants Maton access to the user's accounting account.

Mitigation: Create connections only after user approval, choose the least Zoho scopes needed for the task, and revoke unused or stale connections.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, written to files, or passed through shell arguments.

Mitigation: Use Maton's OAuth flow and credential store where possible, never inspect stored credentials, and send raw HTTP credentials only to api.maton.ai through stdin-based configuration when the CLI is unavailable.

Risk: Operations may target the wrong account when multiple Maton profiles or Zoho Books connections exist.

Mitigation: Specify the intended Maton profile and Zoho Books connection before making API calls, especially before write operations.

Risk: Zoho Books API responses can contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands or prompts, and keep endpoint and recipient choices under user control.

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
- [Related api-gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and an active Zoho Books connection; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
