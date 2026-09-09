## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to read Google Calendar data, check availability, and make approved calendar changes through Maton-managed Google Calendar access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill brokers Google Calendar access through Maton OAuth/API paths and can reach endpoints permitted by the connected account.

Mitigation: Install only when Maton is trusted, prefer OAuth, choose the narrowest available Google scopes, and use read/list calls before changes.

Risk: Calendar writes, connection creation, and connection deletion can affect schedules or revoke automations.

Mitigation: Confirm the exact calendar, account, connection, payload, and intended effect with the user before any write, new connection, or irreversible deletion.

Risk: The raw HTTP fallback uses a long-lived Maton API key and Google Calendar responses may include personal data.

Mitigation: Use the raw API path only when the CLI is unavailable, never print or persist credentials, and extract only the fields needed for the task.

## Reference(s):

- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Google Calendar List Calendars](https://developers.google.com/workspace/calendar/api/v3/reference/calendarList/list)
- [Google Calendar List Events](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Google Calendar Get Event](https://developers.google.com/workspace/calendar/api/v3/reference/events/get)
- [Google Calendar Insert Event](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)
- [Google Calendar Update Event](https://developers.google.com/workspace/calendar/api/v3/reference/events/update)
- [Google Calendar Delete Event](https://developers.google.com/workspace/calendar/api/v3/reference/events/delete)
- [Google Calendar Quick Add Event](https://developers.google.com/workspace/calendar/api/v3/reference/events/quickAdd)
- [Google Calendar Free/Busy Query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTPS request examples, and data-minimization guidance for Google Calendar responses.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
