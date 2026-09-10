## Description:

Zoho Books API integration with managed OAuth for managing invoices, contacts, bills, expenses, and other accounting data through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and accounting operators use this skill to access Zoho Books accounting data through Maton-managed OAuth. It supports reading, creating, updating, and deleting records such as invoices, contacts, bills, expenses, sales orders, and purchase orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or Zoho Books credentials could be exposed if API keys or provider tokens are printed, logged, persisted, or passed through shell commands.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never display or persist credential values, and send Maton API keys only to api.maton.ai when CLI use is unavailable.

Risk: Write, delete, email, invoice, billing, or connection-creation operations can change accounting records or authorize account access.

Mitigation: Default to read/list calls, verify identifiers and account context first, and require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, email, or connection-creation action.

Risk: Requests may affect the wrong Zoho Books account when multiple Maton profiles or Zoho Books connections are available.

Mitigation: Specify the Maton profile and Zoho Books connection ID when more than one account or connection exists, and avoid relying on ambiguous defaults for state-changing operations.

Risk: Zoho Books response content may contain untrusted data that attempts to influence subsequent agent behavior.

Mitigation: Treat API responses as data, validate externally supplied values before reuse, and never execute or follow instructions contained in fetched accounting records, comments, messages, or webhook payloads.

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
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-books)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Zoho Books authorization; normal use defaults to read/list calls and requires explicit confirmation before connection creation, writes, deletes, or email actions.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
