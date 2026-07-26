## Description: <br>
Manages Feishu (Lark) calendars for listing calendars, searching schedules, checking availability, creating events with attendees, and syncing calendar state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and lightweight automation agents use this skill to manage Feishu/Lark calendar workflows such as finding calendars, checking availability, creating reminders or events, and syncing local calendar state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or modify calendar events and shared-calendar settings. <br>
Mitigation: Use a least-privilege Feishu app and require confirmation before event creation, attendee changes, shared-calendar actions, or synchronization. <br>
Risk: Calendar and contact data may be sent to Feishu APIs despite artifact claims about local-only storage. <br>
Mitigation: Treat API communication as expected behavior, limit exposed calendars and contacts, and do not rely on local-only privacy claims. <br>
Risk: Callback URLs may send results to a remote endpoint. <br>
Mitigation: Avoid callback URLs unless the endpoint is trusted and necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-calendar-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-formatted structured responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Feishu app credentials, calendar/contact permissions, and network access to Feishu APIs.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
