## Description: <br>
Check Google Calendar calendars, find free time, schedule meetings, and update events through the Google Calendar API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thejanethmina](https://clawhub.ai/user/thejanethmina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and agents use this skill to review Google Calendar availability, manage events, and coordinate meetings after connecting a Google account through ClawLink. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar write actions can create, update, delete, clear, share, or unshare calendar data. <br>
Mitigation: Preview write actions and proceed only after the user confirms the intended effect, especially for deletion, clearing, attendee changes, and calendar sharing changes. <br>
Risk: Connecting Google Calendar can expose calendar data available to the connected account. <br>
Mitigation: Install only when the user is comfortable connecting Google Calendar through ClawLink and approving calendar access for the agent. <br>
Risk: Scheduling mistakes can occur from timezone ambiguity or creating events without checking availability. <br>
Mitigation: Use IANA timezones and ISO 8601 timestamps with offsets, and check free slots or free/busy data before creating events. <br>


## Reference(s): <br>
- [Google Calendar API Overview](https://developers.google.com/workspace/calendar/api/guides/overview) <br>
- [Google Calendar API Reference](https://developers.google.com/workspace/calendar/api/reference/rest) <br>
- [Google Calendar Event Resource](https://developers.google.com/workspace/calendar/api/reference/rest/v3/events) <br>
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=google-calendar-scheduling) <br>
- [ClawLink OpenClaw Docs](https://docs.claw-link.dev/openclaw) <br>
- [ClawHub Skill Page](https://clawhub.ai/thejanethmina/skills/google-calendar-scheduling) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON tool parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include calendar read and write tool calls; write actions require connection state and user confirmation.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
