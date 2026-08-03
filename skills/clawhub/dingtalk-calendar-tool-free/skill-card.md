## Description: <br>
Helps an agent use the mcporter CLI to manage DingTalk calendar workflows, including creating events, listing schedules, checking free/busy status, booking meeting rooms, updating or deleting events, and searching contacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and developers use this skill to have an AI agent prepare or execute DingTalk calendar operations through mcporter, such as creating meetings, checking schedules and free/busy status, booking rooms, and updating events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar and meeting-room actions can create, update, delete, invite attendees, or book rooms. <br>
Mitigation: Require user confirmation before mutating calendar data, inviting attendees, or booking rooms. <br>
Risk: Calendar, free/busy, contact, and room data may be sent to configured DingTalk or related services. <br>
Mitigation: Use only trusted DingTalk endpoints and credentials, and avoid passing sensitive calendar details unless required. <br>
Risk: The security scan reports mismatched trigger guidance and unclear privacy expectations. <br>
Mitigation: Review each requested action against the DingTalk calendar scope before execution and keep credentials and endpoint configuration under user control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dingtalk-calendar-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call mcporter against configured DingTalk calendar and contact endpoints; outputs can include status, result data, execution logs, and errors.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
