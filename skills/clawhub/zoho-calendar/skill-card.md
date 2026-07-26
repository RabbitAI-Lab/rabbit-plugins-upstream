## Description: <br>
Zoho Calendar API integration with managed OAuth for reading, creating, updating, and deleting calendars and events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to access Zoho Calendar through Maton-managed OAuth, manage calendars, and read, create, update, or delete events, including attendees, reminders, and recurring events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete calendars, events, and OAuth connections in the connected Zoho Calendar account. <br>
Mitigation: Confirm the target calendar or event and intended effect before any create, update, or delete action. <br>
Risk: MATON_API_KEY enables Maton-mediated access to Zoho Calendar data. <br>
Mitigation: Keep MATON_API_KEY private, install only if Maton is trusted with the calendar data, and remove unused OAuth connections. <br>
Risk: When multiple accounts are connected, requests may target the wrong Zoho Calendar account. <br>
Mitigation: Use the Maton-Connection header when multiple accounts are connected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-calendar) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [Maton](https://maton.ai) <br>
- [Zoho Calendar API Introduction](https://www.zoho.com/calendar/help/api/introduction.html) <br>
- [Zoho Calendar Events API](https://www.zoho.com/calendar/help/api/events-api.html) <br>
- [Zoho Calendar Calendars API](https://www.zoho.com/calendar/help/api/calendars-api.html) <br>
- [Create Event](https://www.zoho.com/calendar/help/api/post-create-event.html) <br>
- [Get Events List](https://www.zoho.com/calendar/help/api/get-events-list.html) <br>
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Python, JavaScript, shell command, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations should be confirmed with the user before execution.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
