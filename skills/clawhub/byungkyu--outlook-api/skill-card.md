## Description:

Microsoft Outlook API integration with managed OAuth for reading, sending, and managing emails, folders, calendar events, and contacts via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a user's Outlook mailbox, calendar, folders, and contacts through Maton-managed OAuth. It is suited to read-first Outlook workflows, with explicit user confirmation before writes, connection changes, hosted functions, triggers, or persistent destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outlook authorization may expose email, calendar, folder, and contact data through the connected account.

Mitigation: Authorize only the account and scopes needed for the task, prefer read-only workflows, and revoke unused connections.

Risk: Write operations can send messages, modify folders, delete data, or change calendar events.

Mitigation: List or read first, then confirm the exact target, payload, recipients, and intended effect before any POST, PUT, PATCH, or DELETE action.

Risk: Hosted functions, triggers, and destinations can continue acting or forwarding matching events after setup.

Mitigation: Use user-authored or user-reviewed handlers, deploy with the narrowest network policy, approve each automation separately, and remove automations when the task is complete.

Risk: Raw responses and trigger payloads can contain personal or sensitive data.

Mitigation: Extract only fields needed for the user's task and avoid logging or storing full responses unless the user explicitly asks.

Risk: API keys or OAuth tokens can be exposed if copied into shell environments, files, command lines, or destinations.

Mitigation: Prefer Maton OAuth and the operating system credential store; do not print, export, embed, or inspect credentials.

## Reference(s):

- [ClawHub Outlook Skill](https://clawhub.ai/byungkyu/skills/outlook-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Graph API Overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview)
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar)
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact)
- [Microsoft Graph Query Parameters](https://learn.microsoft.com/en-us/graph/query-parameters)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include Maton CLI commands, Microsoft Graph request examples, hosted function examples, trigger configuration guidance, and user-approval checkpoints.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
