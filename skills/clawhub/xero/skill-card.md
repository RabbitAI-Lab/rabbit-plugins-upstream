## Description:

Xero API integration with managed OAuth for contacts, invoices, payments, accounts, and financial reports through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read and manage Xero accounting resources through Maton-managed OAuth. It supports account setup, connection selection, read/list queries, and confirmed write operations for accounting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access Xero accounting data through a connected Maton account.

Mitigation: Install and use the skill only when Xero access through Maton is intended, prefer OAuth, and choose the narrowest available scopes for the task.

Risk: Write operations can alter contacts, invoices, payments, accounts, or other accounting records.

Mitigation: Default to read/list calls, verify resource identifiers and account context, and require explicit user approval for every POST, PUT, PATCH, or DELETE request.

Risk: Using long-lived API keys or raw HTTP fallback can expose credentials if keys are printed, logged, persisted, or passed on a command line.

Mitigation: Use the Maton CLI with OAuth where possible; if raw HTTP is necessary, keep the key out of logs and command arguments, send it only to api.maton.ai, and rotate it if exposed.

Risk: Multiple Maton profiles or Xero connections can cause actions to target the wrong account.

Mitigation: Specify the intended Maton profile and Xero connection when more than one exists, and confirm the target before any write.

## Reference(s):

- [ClawHub Xero Skill](https://clawhub.ai/byungkyu/skills/xero)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Xero API Overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Payments API](https://developer.xero.com/documentation/api/accounting/payments)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Xero API access; responses may include command examples, request payloads, and review prompts before writes.]

## Skill Version(s):

1.1.0 (source: release evidence; artifact frontmatter version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
