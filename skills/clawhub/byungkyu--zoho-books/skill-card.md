## Description:

Zoho Books API integration with managed OAuth that helps agents read and manage invoices, contacts, bills, expenses, and other accounting data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and accounting operators use this skill to inspect and manage Zoho Books records through authenticated Maton CLI or SDK calls, with read/list defaults and explicit approval before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Zoho Books account can expose or change accounting records.

Mitigation: Confirm the Zoho account and connection before use, prefer read-only scopes where possible, and require explicit confirmation before creating, updating, emailing, voiding, or deleting records.

Risk: Maton credentials or API keys could be exposed if printed, logged, persisted, or passed on a command line.

Mitigation: Use OAuth through the Maton CLI when available, avoid inspecting stored credentials, and only use the raw HTTP/API-key path in constrained environments with stdin-based secret handling.

Risk: Zoho Books responses may contain untrusted external content.

Mitigation: Treat returned records as data, validate them before reuse, and do not execute or follow instructions embedded in fetched content.

## Reference(s):

- [Zoho Books API v3 Introduction](https://www.zoho.com/books/api/v3/introduction/)
- [Zoho Books Invoices API](https://www.zoho.com/books/api/v3/invoices/)
- [Zoho Books Contacts API](https://www.zoho.com/books/api/v3/contacts/)
- [Zoho Books Bills API](https://www.zoho.com/books/api/v3/bills/)
- [Zoho Books Expenses API](https://www.zoho.com/books/api/v3/expenses/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI, SDK, or curl examples for authenticated Zoho Books API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata; skill frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
