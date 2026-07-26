## Description: <br>
Cron Mastery helps agents create reliable cron-based reminders and recurring tasks with one-time cleanup, timezone handling, wake rules, and delivery guidance for WeCom, DingTalk, and Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure precise reminders, recurring jobs, cleanup routines, timezone handling, and message delivery for agent-hosted cron workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad reminder-related phrases may activate persistent scheduling behavior. <br>
Mitigation: Require explicit user confirmation before creating, modifying, or deleting scheduled tasks. <br>
Risk: Persistent reminders and recurring jobs can remain active after the original request is complete. <br>
Mitigation: List existing tasks before creating new ones, use automatic cleanup for one-time reminders, and periodically remove expired jobs. <br>
Risk: External delivery to WeCom, DingTalk, or Feishu can send messages to unintended recipients. <br>
Mitigation: Confirm the delivery channel, recipient, and exact message before sending externally. <br>
Risk: Troubleshooting steps can modify scheduler state or remove local job data. <br>
Mitigation: Back up scheduler state and get user approval before repair actions that delete or rebuild job records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-mastery) <br>
- [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html) <br>
- [Cron expression syntax](https://crontab.guru/) <br>
- [WeCom webhook documentation](https://developer.work.weixin.qq.com/document/path/91770) <br>
- [DingTalk custom robot access](https://open.dingtalk.com/document/robots/custom-robot-access) <br>
- [Feishu card JSON structure](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/feishu-cards/card-json-structure) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with JSON task payload examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create persistent scheduled tasks, write timezone preferences, and send configured enterprise chat messages when the host agent has those permissions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
