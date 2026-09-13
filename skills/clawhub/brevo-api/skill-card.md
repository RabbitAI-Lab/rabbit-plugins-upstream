## Description:

Brevo API integration with managed OAuth for email marketing, transactional emails, SMS, contacts, and CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to work with Brevo accounts through Maton-managed OAuth, including email marketing, transactional email, SMS, contacts, lists, templates, campaigns, and CRM workflows. The skill defaults to read and list operations and requires user confirmation for writes, new connections, hosted functions, triggers, and persistent destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brevo writes can send email, change contacts, alter templates or lists, and affect campaigns in the connected account.

Mitigation: Default to read and list calls, confirm the exact Brevo account and connection, and obtain explicit user approval before any POST, PUT, PATCH, DELETE, campaign send, or new connection.

Risk: Long-lived API keys or environment variables can expose account access beyond the immediate task.

Mitigation: Prefer Maton OAuth and operating-system credential storage; use raw HTTP or MATON_API_KEY only where the CLI cannot be installed and avoid logging or persisting credentials.

Risk: Hosted functions, triggers, and destinations can create persistent automation or data forwarding flows.

Mitigation: Review the function, trigger, destination host, payload fields, and persistence with the user before creation or updates, and keep destinations on Maton-controlled endpoints unless the user explicitly approves an external host.

## Reference(s):

- [Brevo API Overview](https://developers.brevo.com/)
- [Brevo API Key Concepts](https://developers.brevo.com/docs/how-it-works)
- [Manage Contacts](https://developers.brevo.com/docs/synchronise-contact-lists)
- [Send Transactional Email](https://developers.brevo.com/docs/send-a-transactional-email)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brevo-api)
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

**Output Format:** [Markdown guidance with inline code blocks, JSON examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Brevo API calls, Maton CLI commands, hosted function snippets, trigger configuration, and safety checks for user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
