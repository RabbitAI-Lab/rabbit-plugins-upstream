## Description:

Zoho Books API integration with managed OAuth for managing invoices, contacts, bills, expenses, and other accounting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help an agent read, create, update, and delete Zoho Books accounting records through the Maton gateway. It is intended for workflows involving contacts, invoices, bills, expenses, sales orders, purchase orders, and related financial data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Zoho Books accounting records, including invoices, contacts, bills, and expenses.

Mitigation: Review requested OAuth scopes, prefer read-only access when possible, and require clear user confirmation before creating, editing, emailing, voiding, or deleting financial records.

Risk: Financial writes may affect the wrong account or record if a default connection or profile is ambiguous.

Mitigation: Verify account context and resource identifiers before write operations, and specify the intended connection or profile when more than one is available.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, saved, or passed through shell commands.

Mitigation: Use managed OAuth or the operating system credential store, avoid exposing long-lived API keys, and never print, persist, or transmit credential values outside the intended gateway.

## Reference(s):

- [ClawHub Zoho Books Skill](https://clawhub.ai/byungkyu/skills/zoho-books)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Books API v3 Introduction](https://www.zoho.com/books/api/v3/introduction/)
- [Zoho Books Invoices API](https://www.zoho.com/books/api/v3/invoices/)
- [Zoho Books Contacts API](https://www.zoho.com/books/api/v3/contacts/)
- [Zoho Books Bills API](https://www.zoho.com/books/api/v3/bills/)
- [Zoho Books Expenses API](https://www.zoho.com/books/api/v3/expenses/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose API calls that require network access, OAuth authorization, and user confirmation for writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
