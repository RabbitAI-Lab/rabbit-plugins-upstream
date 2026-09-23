## Description:

Provides practical guidance for reliable scheduled reminders and recurring agent tasks by preferring cron-style scheduling over long heartbeat waits, with timezone handling, cleanup guidance, and WeCom, DingTalk, and Feishu notification examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create reliable one-time and recurring reminders, manage task cleanup, lock timezone assumptions, and troubleshoot scheduling failures in agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or delete scheduled tasks.

Mitigation: Review and approve each proposed schedule, task name, payload, and cleanup action before execution.

Risk: The skill may write timezone information to persistent memory.

Mitigation: Confirm the intended timezone with the user before saving or changing persistent state.

Risk: The skill may send reminder content to third-party chat platforms.

Mitigation: Confirm the channel, recipient, and exact message content before sending notifications.

Risk: The skill may run command-line troubleshooting steps.

Mitigation: Limit shell commands to the smallest required diagnostic or cleanup action and review file paths before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/cron-mastery)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)
- [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html)
- [Cron expression syntax](https://crontab.guru/)
- [WeCom webhook documentation](https://developer.work.weixin.qq.com/document/path/91770)
- [DingTalk custom robot documentation](https://open.dingtalk.com/document/robots/custom-robot-access)
- [Feishu card JSON documentation](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/feishu-cards/card-json-structure)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, JSON]

**Output Format:** [Markdown guidance with JSON scheduling examples and command-line troubleshooting steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose scheduled tasks, timezone memory updates, task cleanup actions, and third-party chat notification settings.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
