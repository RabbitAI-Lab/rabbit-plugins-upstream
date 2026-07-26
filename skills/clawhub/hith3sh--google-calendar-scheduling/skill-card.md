## Description: <br>
Check Google Calendar calendars, find free time, schedule meetings, and update events via the Google Calendar API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hith3sh](https://clawhub.ai/user/hith3sh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to connect Google Calendar through ClawLink, inspect calendars and availability, and create, update, move, or delete events after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Google Calendar data through the connected account. <br>
Mitigation: Install only if the user is comfortable connecting Google Calendar through ClawLink and review prompts before approving write actions. <br>
Risk: Deleting calendars, clearing events, moving events, deleting events with attendees, or changing sharing permissions can have high-impact effects. <br>
Mitigation: Preview and explicitly confirm destructive or sharing-related actions before execution, especially when attendees or other users are affected. <br>
Risk: Creating events without checking availability can introduce scheduling conflicts. <br>
Mitigation: Use free/busy or free-slot checks before creating calendar events when conflict avoidance matters. <br>


## Reference(s): <br>
- [Google Calendar Skill Page](https://clawhub.ai/hith3sh/skills/google-calendar-scheduling) <br>
- [Google Calendar API Overview](https://developers.google.com/workspace/calendar/api/guides/overview) <br>
- [Google Calendar API Reference](https://developers.google.com/workspace/calendar/api/reference/rest) <br>
- [Google Calendar Event Resource](https://developers.google.com/workspace/calendar/api/reference/rest/v3/events) <br>
- [ClawLink Docs](https://docs.claw-link.dev/openclaw) <br>
- [ClawLink Verification](https://claw-link.dev/verify) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON tool parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ClawLink tool calls; write operations require preview and explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
