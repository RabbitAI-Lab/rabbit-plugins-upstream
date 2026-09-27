## Description:

Xero API integration with managed OAuth for managing contacts, invoices, payments, accounts, bank transactions, and financial reports through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external accountants, and developers use this skill to work with Xero accounting data through authenticated Maton-mediated API calls. It supports read-first accounting workflows and user-approved writes or hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated Xero access can expose or change sensitive accounting data.

Mitigation: Install only when Xero access through Maton is intended, prefer read and list calls first, and confirm every write or new connection separately.

Risk: Broad OAuth scopes or long-lived API keys can grant more access than the current task requires.

Mitigation: Review OAuth scopes carefully, choose only the scopes needed for the task, and avoid raw API-key use unless the CLI is unavailable.

Risk: Triggers and destinations can continue forwarding event data after setup.

Mitigation: Create automation only after explicit approval, review the trigger source and destination, and remove unneeded triggers or destinations when the task is complete.

## Reference(s):

- [Xero Skill on ClawHub](https://clawhub.ai/byungkyu/skills/xero)
- [byungkyu ClawHub Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Xero API Overview](https://developer.xero.com/documentation/api/accounting/overview)
- [Xero Contacts API](https://developer.xero.com/documentation/api/accounting/contacts)
- [Xero Invoices API](https://developer.xero.com/documentation/api/accounting/invoices)
- [Xero Accounts API](https://developer.xero.com/documentation/api/accounting/accounts)
- [Xero Payments API](https://developer.xero.com/documentation/api/accounting/payments)
- [Xero Reports API](https://developer.xero.com/documentation/api/accounting/reports)
- [Maton Docs](https://docs.maton.ai)
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

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include authenticated Maton CLI commands, raw HTTP examples for constrained environments, and user-approval guidance for writes or automation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
