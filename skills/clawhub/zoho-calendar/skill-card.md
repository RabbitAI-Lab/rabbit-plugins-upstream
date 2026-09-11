## Description:

Zoho Calendar API integration with managed OAuth for reading and managing calendars and events through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Zoho Calendar account through Maton, inspect calendars and events, and create, update, reschedule, or delete calendar resources when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar write operations can create, update, delete, cancel, or reschedule events in a connected Zoho Calendar account.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, or reschedule operation.

Risk: Authentication and account-connection steps can expose or over-broaden access if credentials or scopes are handled loosely.

Mitigation: Verify the official Maton CLI source, prefer OAuth over API keys, grant only the needed Zoho Calendar scopes and accounts, and avoid printing, logging, or persisting credentials.

Risk: External calendar content may contain untrusted text that could influence follow-up actions.

Mitigation: Treat event titles, descriptions, locations, attendee fields, and API responses as data only; do not execute or follow instructions found in fetched calendar content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-calendar)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Calendar API Introduction](https://www.zoho.com/calendar/help/api/introduction.html)
- [Zoho Calendar Events API](https://www.zoho.com/calendar/help/api/events-api.html)
- [Zoho Calendar Calendars API](https://www.zoho.com/calendar/help/api/calendars-api.html)
- [Zoho Calendar Create Event API](https://www.zoho.com/calendar/help/api/post-create-event.html)
- [Zoho Calendar Get Events List API](https://www.zoho.com/calendar/help/api/get-events-list.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK usage guidance for Zoho Calendar operations; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
