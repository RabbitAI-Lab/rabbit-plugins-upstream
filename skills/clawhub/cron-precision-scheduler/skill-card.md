## Description: <br>
Provides reliable scheduled reminders and recurring task guidance using cron-style scheduling, timezone locking, wake rules, cleanup, and optional WeCom, DingTalk, or Feishu message delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create precise reminders and recurring agent tasks, choose cron scheduling instead of heartbeat waits for delays longer than one minute, and troubleshoot scheduler failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide agents to write persistent timezone memory or alter scheduler state. <br>
Mitigation: Confirm the intended timezone and task details before writing memory or changing scheduler records. <br>
Risk: Repair steps can involve deleting jobs.json or restarting the Agent platform, which may remove scheduled tasks. <br>
Mitigation: Back up scheduler state and record task recreation details before deleting state files or restarting the platform. <br>
Risk: External message delivery can fail if WeCom, DingTalk, or Feishu channel and recipient settings are wrong or expired. <br>
Mitigation: Verify channel, recipient, and webhook settings before relying on reminders, and keep a fallback delivery channel for important tasks. <br>


## Reference(s): <br>
- [ISO 8601 Date and Time Format](https://www.iso.org/iso-8601-date-and-time-format.html) <br>
- [Crontab Guru](https://crontab.guru/) <br>
- [WeCom Webhook Documentation](https://developer.work.weixin.qq.com/document/path/91770) <br>
- [DingTalk Custom Robot Access](https://open.dingtalk.com/document/robots/custom-robot-access) <br>
- [Feishu Card JSON Structure](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/feishu-cards/card-json-structure) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, Text] <br>
**Output Format:** [Markdown guidance with JSON cron task examples and command-style scheduler steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes timezone, wake, cleanup, and troubleshooting instructions for agent scheduler state.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
