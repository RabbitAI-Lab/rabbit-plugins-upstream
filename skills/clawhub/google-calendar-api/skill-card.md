## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and manage Google Calendar calendars, events, availability, and scheduling through Maton OAuth. It supports read-first calendar workflows and requires user approval before creating connections or changing calendar data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar writes or meeting changes can notify participants or alter a user's schedule.

Mitigation: Default to read/list calls, verify the target calendar or event, and require explicit user approval before create, update, delete, quick-add, or reschedule operations.

Risk: Using a long-lived API key or exposing credentials in logs, files, or command lines can leak access to Maton or Google Calendar.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store; never print, persist, or pass credentials on command lines.

Risk: Multiple Maton accounts or Google Calendar connections can send requests to the wrong account.

Mitigation: Confirm the active profile and specify the intended connection before writes or sensitive reads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Google Calendar List Calendars](https://developers.google.com/workspace/calendar/api/v3/reference/calendarList/list)
- [Google Calendar List Events](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Google Calendar FreeBusy Query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read/list operations first; write, delete, reschedule, quick-add, and connection operations require user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
