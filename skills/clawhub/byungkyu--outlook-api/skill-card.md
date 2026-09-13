## Description:

Outlook helps agents use Microsoft Graph through Maton-managed OAuth to read, send, and manage Outlook email, folders, calendar events, and contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an Outlook account, make approved Microsoft Graph calls, and optionally set up narrowly scoped Maton functions or triggers for Outlook-related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Outlook mail, calendar, and contact data through an authorized Maton connection.

Mitigation: Use OAuth where possible, select only the scopes needed for the task, and make read-only calls before any write action.

Risk: Sending email, creating events, deleting resources, or changing connections can affect the user's Outlook account.

Mitigation: Get explicit user approval for every write, send, delete, new connection, hosted function, trigger, or destination change; prefer drafts before sending mail.

Risk: Triggers and external destinations can create ongoing disclosure of Outlook-adjacent or third-party app data.

Mitigation: Keep triggers narrowly scoped, forward only required fields, prefer Maton-hosted destinations, and use third-party destination URLs only after the user approves the exact host and data flow.

Risk: Long-lived API keys or credentials in headers, templates, logs, files, or child process environments can expose account access.

Mitigation: Prefer OAuth and the operating system credential store, avoid exporting API keys, never place provider or Maton credentials in destination headers or body templates, and rotate exposed keys.

## Reference(s):

- [Outlook Skill Page](https://clawhub.ai/byungkyu/skills/outlook-api)
- [Maton Homepage](https://maton.ai)
- [Microsoft Graph API Overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview)
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar)
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact)
- [Microsoft Graph Query Parameters](https://learn.microsoft.com/en-us/graph/query-parameters)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference user-authorized Outlook data and should be reviewed before writes, sends, deletes, or automation changes.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
