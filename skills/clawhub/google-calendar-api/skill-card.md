## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to let an agent perform approved Google Calendar reads and writes through Maton, including event management, calendar listing, and availability checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar credentials or API keys could be exposed if printed, exported, embedded in trigger destinations, or stored in files.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, avoid long-lived API keys where possible, and never print, inspect, transmit, or embed Maton or provider credentials.

Risk: Calendar writes, connection changes, and deletions can modify user schedules or grant broader account access than intended.

Mitigation: Default to read and list operations, use least-privilege scopes, specify the intended account or connection, and confirm each write or connection change with the target, payload, and effect.

Risk: Hosted functions, triggers, and destinations can create persistent automation or forwarding of event data.

Mitigation: Use only user-reviewed functions, keep functions private, apply DENY_ALL network policy by default, prefer Maton-controlled destinations, and remove unused functions, triggers, and destinations when finished.

Risk: Third-party API responses and event payloads may contain personal data or adversarial instructions.

Mitigation: Treat fetched content as data, extract only fields needed for the task, avoid logging raw payloads, and do not execute or interpolate external content into commands.

## Reference(s):

- [ClawHub Google Calendar Skill](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Google Calendar CalendarList.list](https://developers.google.com/workspace/calendar/api/v3/reference/calendarList/list)
- [Google Calendar Events.list](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Google Calendar Events.insert](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)
- [Google Calendar FreeBusy.query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Maton CLI commands and Google Calendar API calls; write, connection, function, trigger, and destination actions require user confirmation.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
