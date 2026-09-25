## Description:

钉钉日历支持创建日程、查询空闲状态与预订会议室，实现钉钉日程管理的自动化操作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill through an agent to create DingTalk calendar events, check availability, and reserve meeting rooms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, or book DingTalk calendar resources, which could affect organizational schedules.

Mitigation: Require explicit user approval before creating, modifying, or booking calendar resources.

Risk: The trust and configuration of mcporter and the DingTalk protocol server are under-specified.

Mitigation: Verify mcporter and the DingTalk protocol server are trusted and correctly configured before installing or using the skill.

Risk: The security summary flags the release for review because scope, dependencies, and confirmation expectations are under-specified.

Mitigation: Review before installing and limit use to DingTalk calendar tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dingtalk-calendar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires trusted mcporter and DingTalk protocol server configuration.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
