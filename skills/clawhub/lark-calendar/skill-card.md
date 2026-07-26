## Description: <br>
Create, update, and delete calendar events and tasks in Lark (Feishu), including employee directory support for name-to-user_id resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[boyangwang](https://clawhub.ai/user/boyangwang) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Employees and operators in a configured Lark workspace use this skill to create, update, list, and delete calendar events and tasks, including resolving coworker names to Lark user IDs for attendees and assignees. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags under-disclosed messaging capability in addition to the documented calendar and task behavior. <br>
Mitigation: Review or disable unused message-sending helpers and grant messaging scopes only if messaging is an intended, documented use. <br>
Risk: Broad employee-directory access and static employee data may expose or preserve workspace identity details beyond the immediate scheduling task. <br>
Mitigation: Restrict Lark contact scopes to the minimum needed for name resolution and audit, update, or remove fallback employee records before deployment. <br>
Risk: The skill automatically adds Boyang to new calendar events and defaults to the documented Claw calendar. <br>
Mitigation: Confirm this behavior is acceptable for the target workspace, and override or modify the default calendar and attendee behavior before use if needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/boyangwang/skills/lark-calendar) <br>
- [Lark Calendar Events API](https://open.larksuite.com/document/server-docs/calendar-v4/calendar-event/create) <br>
- [Lark Calendar Attendees API](https://open.larksuite.com/document/server-docs/calendar-v4/calendar-event-attendee/create) <br>
- [Lark Tasks API](https://open.larksuite.com/document/server-docs/task-v2/task/create) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JavaScript module usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FEISHU_APP_ID and FEISHU_APP_SECRET for a configured Lark app; command outputs may include event, task, attendee, assignee, or URL details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
