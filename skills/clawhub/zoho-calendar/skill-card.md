## Description:

Zoho Calendar API integration with managed OAuth for reading, creating, updating, deleting, and managing calendars and events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to connect a Zoho Calendar account through Maton and perform calendar and event scheduling workflows through guided API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, change, or delete Zoho Calendar events after authorization.

Mitigation: Default to read/list calls, confirm the target resource and intended effect before any write, and revoke unused connections when no longer needed.

Risk: A connected account may expose calendar data and OAuth scopes beyond the immediate task.

Mitigation: Prefer OAuth, review requested Zoho scopes, select the least privilege available, and use the intended Maton profile and connection explicitly.

Risk: Calendar content and API responses may include untrusted external data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and pass values as discrete arguments or via stdin.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-calendar)
- [Maton](https://maton.ai)
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

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and an active Zoho Calendar connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
