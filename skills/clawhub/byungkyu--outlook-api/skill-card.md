## Description:

Microsoft Outlook API integration with managed OAuth for reading, sending, and managing email, folders, calendar events, and contacts via Microsoft Graph through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to work with a user-authorized Outlook account: reviewing mailbox or calendar data, drafting or sending messages, and managing folders, events, and contacts through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify mailbox, calendar, and contact data through user-authorized Maton access.

Mitigation: Install only when Maton-mediated Outlook access is acceptable; use OAuth, connect only needed accounts and scopes, and require explicit confirmation before sending email, deleting items, or changing calendar/contact data.

Risk: Using a long-lived Maton API key instead of OAuth increases the chance of credential exposure.

Mitigation: Prefer the Maton CLI OAuth flow; use the raw HTTP/API-key fallback only when the CLI cannot be installed, and never print, log, or persist the key.

Risk: Mailbox, calendar, and contact content can contain untrusted text.

Mitigation: Treat fetched Outlook content as data, not instructions, and do not execute or interpolate it into shell commands or follow-up API actions without validation and user confirmation.

## Reference(s):

- [Outlook skill page](https://clawhub.ai/byungkyu/skills/outlook-api)
- [Maton homepage](https://maton.ai)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview)
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar)
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact)
- [Microsoft Graph query parameters](https://learn.microsoft.com/en-us/graph/query-parameters)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [shell commands, API calls, configuration, code, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-authorized Outlook connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
