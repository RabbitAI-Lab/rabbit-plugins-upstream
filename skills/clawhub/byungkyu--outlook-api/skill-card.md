## Description:

Microsoft Outlook API integration with managed OAuth for reading, sending, and managing emails, folders, calendar events, and contacts via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with a user-authorized Outlook account through Maton and Microsoft Graph. It supports email, folder, calendar, and contact workflows while defaulting to read/list operations and requiring confirmation before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Outlook messages, folders, calendar events, and contacts through a connected account.

Mitigation: Use OAuth, connect only the account needed for the task, authorize the narrowest available scopes, and revoke unused connections.

Risk: Write operations can send email, modify records, delete data, or change calendar state.

Mitigation: Default to read/list operations and require explicit confirmation of the target resource, payload, and intended effect before every send, update, delete, or new connection.

Risk: Long-lived Maton API keys can leak if printed, persisted, passed on command lines, or sent to the wrong host.

Mitigation: Prefer OAuth and the Maton CLI; if an API key is unavoidable, keep it out of logs and files, pass it through the environment only, and send it only to api.maton.ai.

Risk: Outlook content returned by the API can contain untrusted or adversarial instructions.

Mitigation: Treat fetched messages, contact fields, and event data as data only; do not execute embedded instructions or let them choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/outlook-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview)
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar)
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact)
- [Microsoft Graph query parameters](https://learn.microsoft.com/en-us/graph/query-parameters)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, Microsoft Graph API paths, SDK snippets, and confirmation guidance for sensitive actions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
