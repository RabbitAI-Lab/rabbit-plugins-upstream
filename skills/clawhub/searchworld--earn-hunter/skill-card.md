## Description: <br>
Automatically monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends notifications, and guides users through subscription steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OKX users and agent operators use this skill to monitor OKX Earn opportunities, configure APY and currency filters, receive Telegram, Lark, or session notifications, and follow subscription guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs persistent background monitoring for OKX Earn opportunities. <br>
Mitigation: Review the scheduler it creates and the files under ~/.okx/earn-hunter before enabling scheduled scans. <br>
Risk: The skill uses financial-account context and includes transaction guidance. <br>
Mitigation: Confirm OKX account permissions and require separate explicit confirmation for purchase, redeem, or transfer steps. <br>
Risk: The skill can send external notifications through Telegram or Lark. <br>
Mitigation: Verify the configured notification destination before relying on scheduled monitoring. <br>


## Reference(s): <br>
- [Earn Hunter on ClawHub](https://clawhub.ai/searchworld/skills/earn-hunter) <br>
- [Publisher profile](https://clawhub.ai/user/searchworld) <br>
- [OKX](https://www.okx.com) <br>
- [Configuration Reference](references/config-reference.md) <br>
- [Notification Channels](references/notify-channels.md) <br>
- [Purchase Guide](references/purchase-guide.md) <br>
- [Scan Logic](references/scan-logic.md) <br>
- [Scheduler Setup](references/scheduler-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces monitoring setup guidance, scan summaries, notification content, and subscription guidance; financial actions require separate explicit confirmation.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
