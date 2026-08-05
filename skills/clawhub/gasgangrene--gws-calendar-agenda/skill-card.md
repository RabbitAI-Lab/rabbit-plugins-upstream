## Description: <br>
Google Calendar: Show upcoming events across all calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to help users view upcoming Google Calendar events across all calendars, with options to narrow the agenda by day, date range, calendar, or timezone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default agenda view queries all calendars unless filtered. <br>
Mitigation: Use the --calendar flag when the agent should limit results to a specific calendar. <br>
Risk: The skill depends on Google Calendar access through the gws CLI. <br>
Mitigation: Install only when the agent is intended to read Google Calendar agenda data, and review Google account permissions before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/gws-calendar-agenda) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only agenda guidance for the gws command-line tool.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
