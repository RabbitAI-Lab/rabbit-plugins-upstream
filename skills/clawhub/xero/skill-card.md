## Description:

Xero API integration with managed OAuth for managing contacts, invoices, payments, accounts, and financial reports through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, finance operators, and developers use this skill to inspect and update Xero accounting data through authenticated API calls. It is suited for tasks such as listing contacts, preparing invoices, reviewing payments, and running financial reports after user-approved connection setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xero requests are routed through Maton and require access to the selected Xero tenant.

Mitigation: Confirm that Maton is an acceptable gateway for the task and authorize only the Xero tenant and scopes needed.

Risk: Financial write operations can create or change contacts, invoices, payments, accounts, or related accounting records.

Mitigation: Review the exact resource, payload, target connection, and intended effect with the user before any POST, PUT, PATCH, or DELETE request.

Risk: Ambiguous Maton profiles or Xero connections can send requests to the wrong account.

Mitigation: List available connections first and specify the intended connection when more than one Xero connection or Maton profile exists.

## Reference(s):

- [Xero skill on ClawHub](https://clawhub.ai/byungkyu/skills/xero)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Xero API Overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Accounts API](https://developer.xero.com/documentation/api/accounting/accounts)
- [Xero Payments API](https://developer.xero.com/documentation/api/accounting/payments)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Xero API requests through Maton and emphasize read-first workflows plus explicit approval before writes.]

## Skill Version(s):

1.2.0 (source: server release metadata; skill frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
