## Description:

Brevo API integration with managed OAuth for email marketing, transactional email, SMS, contacts, campaigns, lists, templates, and CRM tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to authenticate through Maton and make approved Brevo API calls for contacts, lists, email campaigns, transactional messages, templates, senders, and related CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real email campaigns and modify or delete Brevo business data when approved.

Mitigation: Default to read and list calls, verify account context and identifiers first, and require explicit confirmation of the target, payload, recipients, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Raw API-key fallback can expose a long-lived Maton credential if the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is necessary, read the key only from the process environment, never print or persist it, and send it only to api.maton.ai.

Risk: Functions, triggers, and destinations can create persistent automation or ongoing data forwarding.

Mitigation: Require separate approval for each hosted function, trigger, invocation, and destination; disclose destination host, payload fields, persistence, and credential handling; remove automation when no longer needed.

## Reference(s):

- [ClawHub Brevo Skill](https://clawhub.ai/byungkyu/skills/brevo-api)
- [Maton Homepage](https://maton.ai)
- [Brevo API Overview](https://developers.brevo.com/)
- [Brevo API Key Concepts](https://developers.brevo.com/docs/how-it-works)
- [Manage Contacts](https://developers.brevo.com/docs/synchronise-contact-lists)
- [Send Transactional Email](https://developers.brevo.com/docs/send-a-transactional-email)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with inline shell, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task-specific Brevo API guidance and commands; write operations and automation setup require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
