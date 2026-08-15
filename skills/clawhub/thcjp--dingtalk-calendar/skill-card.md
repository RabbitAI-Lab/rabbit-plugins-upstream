## Description:

钉钉日历 helps agents handle DingTalk calendar workflows, including event creation, availability checks, schedule queries, and meeting-room reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, assistants, and workspace operators use this skill to automate DingTalk scheduling tasks such as creating events, checking availability, querying calendars, and reserving meeting rooms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect organizational schedules and meeting rooms, and the security evidence says write-action limits are not clearly scoped.

Mitigation: Limit use to explicit DingTalk calendar requests and require confirmation before creating or modifying events or reserving meeting rooms.

Risk: The security evidence recommends review before installing in an agent with command execution.

Mitigation: Deploy only with constrained command execution for the required calendar workflow and keep unrelated files outside the calendar skill context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dingtalk-calendar)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce DingTalk calendar operation guidance, mcporter CLI calls, JSON argument examples, and troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
