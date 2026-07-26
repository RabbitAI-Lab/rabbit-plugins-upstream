## Description: <br>
Automatically monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends push notifications, and guides subscription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External crypto users and agent operators use this skill to configure recurring OKX Earn monitoring, receive opportunity notifications, and follow guided subscription workflows with explicit confirmation for account actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires authenticated OKX access and may read account and Earn product data through the OKX CLI. <br>
Mitigation: Use the OKX CLI authentication flow rather than sharing credentials in chat, and install only when the user accepts this account-data access. <br>
Risk: Recurring background scans may run through OpenClaw cron or OS crontab and send notifications outside the current agent session. <br>
Mitigation: Confirm the scheduler type, scan interval, notification channel, state directory, and log locations before activation. <br>
Risk: Guided subscription flows can involve crypto transfer, redemption, or purchase commands. <br>
Mitigation: Require explicit user confirmation before every transfer, redemption, purchase, or subscription command is executed. <br>
Risk: Telegram or Lark notification setup can expose alerts to external channels. <br>
Mitigation: Validate the selected channel, avoid accepting secrets directly in chat, and verify a test notification before enabling recurring scans. <br>


## Reference(s): <br>
- [Configuration Reference](references/config-reference.md) <br>
- [Notification Channels](references/notify-channels.md) <br>
- [Purchase Guide](references/purchase-guide.md) <br>
- [Scan Logic](references/scan-logic.md) <br>
- [Scheduler Setup](references/scheduler-setup.md) <br>
- [OKX](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notifications and guidance with shell commands and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local OKX Earn Hunter state, scheduler entries, notification logs, and Telegram or Lark notification payloads.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
