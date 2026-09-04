## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules through the Maton CLI or API gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to interact with Google Calendar accounts through Maton-managed OAuth, including reading calendars, checking free/busy availability, and creating, updating, or deleting events with explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or modify Google Calendar data after account authorization.

Mitigation: Use OAuth where possible, approve connection creation and every calendar-changing action explicitly, and specify the intended connection when multiple accounts exist.

Risk: Long-lived Maton API keys or stored credentials could be exposed if printed, logged, exported, or passed through shell commands.

Mitigation: Avoid exposing MATON_API_KEY or stored credentials; prefer Maton OAuth and let the CLI use the operating system credential store.

Risk: Calendar writes such as creating, cancelling, or rescheduling meetings can notify participants or affect schedules.

Mitigation: Default to read and list operations first, then confirm the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE operations.

Risk: Calendar API responses may contain untrusted external content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or follow instructions found inside fetched calendar content.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Google Calendar Events: List](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Google Calendar Events: Insert](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)
- [Google Calendar Freebusy: Query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Calendar connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
