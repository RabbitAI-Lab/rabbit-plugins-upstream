## Description:

Xero API integration with managed OAuth for managing contacts, invoices, payments, accounts, bank transactions, and financial reports through the Maton CLI and gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and manage Xero accounting data through Maton-managed OAuth. It supports common accounting workflows such as listing contacts, creating invoices, recording payments, reviewing accounts, and running financial reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create connections, delete connections, and write to accounting data.

Mitigation: Require explicit user confirmation before connection creation, deletion, or any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys or provider tokens could be exposed if printed, logged, or stored outside the credential store.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, and never print, persist, or pass secrets on command lines.

Risk: A user with multiple Xero connections or Maton profiles could accidentally operate on the wrong account.

Mitigation: Specify the intended connection and profile whenever more than one account is available.

Risk: External Xero data may contain untrusted content.

Mitigation: Treat API responses as data and do not execute, evaluate, or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Xero Skill](https://clawhub.ai/byungkyu/skills/xero)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Xero API Overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may perform Xero API calls through Maton and require explicit user approval before connection creation or accounting data writes.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
