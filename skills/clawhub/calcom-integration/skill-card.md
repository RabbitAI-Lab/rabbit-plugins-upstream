## Description: <br>
Integrate with Cal.com to list event types, create or cancel bookings, retrieve available slots, manage availability schedules, and fetch user information through the Cal.com REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a Cal.com account for booking, availability, and event-type workflows. It is useful when an agent needs to inspect calendar configuration, propose available times, or perform user-confirmed booking and schedule changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Cal.com API key can grant read and write access to bookings and availability. <br>
Mitigation: Use the minimum Cal.com API scopes required and store the API key in a secret store rather than in prompts, logs, or shared files. <br>
Risk: Creating or canceling bookings and replacing availability schedules can change real calendar state. <br>
Mitigation: Require a clear preview and explicit user confirmation before creating bookings, canceling bookings, or submitting schedule changes. <br>
Risk: Timezone or daylight-saving mistakes can create bookings at the wrong time. <br>
Mitigation: Confirm the intended timezone with the user and send ISO 8601 timestamps with UTC offsets or UTC values. <br>
Risk: Availability schedule updates may replace the full schedule rather than merge individual fields. <br>
Mitigation: Fetch the current schedule first, preserve required fields, and submit a complete reviewed schedule object. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gaolfun/skills/calcom-integration) <br>
- [Cal.com](https://cal.com) <br>
- [Cal.com REST API Base URL](https://api.cal.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON examples and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses structured success and error JSON blocks for API operation results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
