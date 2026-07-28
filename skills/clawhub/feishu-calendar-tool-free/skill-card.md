## Description: <br>
飞书日历基础版 helps an agent manage Feishu/Lark calendars by listing calendars, searching events, checking availability, creating events with attendees, and syncing schedule state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent perform light Feishu/Lark calendar operations such as creating reminders, checking schedules, listing calendars, and syncing calendar state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar read/write access, contacts-read access, and app secret access can expose sensitive scheduling and identity data. <br>
Mitigation: Verify Feishu/Lark app permissions before installation and scope credentials to the minimum needed. <br>
Risk: Calendar write and sharing actions can create events, add attendees, set shared calendar permissions, or send callback notifications. <br>
Mitigation: Require explicit user confirmation before write, sharing, attendee, permission, or callback operations. <br>
Risk: The security summary reports conflicting privacy and capability claims and under-disclosed high-impact calendar sharing/API behavior. <br>
Mitigation: Treat sharing and API behavior as high impact, review proposed changes before execution, and test in a non-production calendar first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-calendar-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON response examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Feishu/Lark app credentials and explicit confirmation for calendar write operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
