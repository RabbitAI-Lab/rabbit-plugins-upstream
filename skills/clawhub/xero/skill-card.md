## Description:

Guides agents in managing Xero contacts, invoices, payments, accounts, and financial reports through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a connected Xero organization use this skill to look up accounting records, prepare approved updates, and run financial reports. With separate approval, they can configure scheduled or event-driven actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing access to the wrong Xero organization or granting unnecessarily broad access.

Mitigation: Confirm the intended organization and use read-only or narrow scopes where possible.

Risk: Accounting records may be changed in the wrong connection or without the user's intent.

Mitigation: Verify the target connection and obtain explicit approval before each write.

Risk: Functions, triggers, or destinations may perform or forward actions automatically.

Mitigation: Review the data, action, and destination before enabling each automation.

## Reference(s):

- [Xero Accounting API overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Scheduled trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and authorization for the intended Xero organization.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
