## Description: <br>
Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read and manage Google Calendar calendars, events, connections, and availability through Maton-managed OAuth and API or CLI examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Google Calendar data through Maton-mediated access. <br>
Mitigation: Install only if Maton-mediated calendar access is acceptable, and confirm the target calendar, event, connection, and intended effect before create, update, delete, or connection-management commands. <br>
Risk: Multiple Google Calendar connections can cause requests to affect the wrong account or calendar. <br>
Mitigation: Specify the intended connection when multiple Google Calendar connections exist and verify the target resource before write operations. <br>


## Reference(s): <br>
- [ClawHub Google Calendar Skill](https://clawhub.ai/byungkyu/skills/google-calendar-api) <br>
- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference) <br>
- [Google Calendar Events Reference](https://developers.google.com/workspace/calendar/api/v3/reference/events/list) <br>
- [Google Calendar Free/Busy Reference](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with API endpoint examples and inline bash, Python, and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Google Calendar OAuth connection.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
