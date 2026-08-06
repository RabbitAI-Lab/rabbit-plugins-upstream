## Description: <br>
Monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends notifications, and guides users through subscription steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satawat10](https://clawhub.ai/user/satawat10) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OKX users and agent operators use this skill to configure recurring Earn product scans, receive opportunity alerts, and get guided next steps for subscriptions. It is intended for monitoring and decision support around OKX Earn products, not autonomous trading without user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates persistent scheduled monitoring jobs and local files under the user's OKX configuration area. <br>
Mitigation: Review the configured scheduler, notification destination, and local earn-hunter files before and after activation. <br>
Risk: The artifact includes guidance for subscribe, transfer, and redeem workflows that can affect account balances. <br>
Mitigation: Require explicit user confirmation of asset, amount, term, and account impact before any account-changing command; prefer the OKX app or a dedicated execution skill for purchases. <br>
Risk: Notifications can be sent through external Telegram or Lark destinations. <br>
Mitigation: Confirm webhook and chat destinations during setup and avoid sharing credentials in chat; use environment variables or the OKX CLI's own authentication storage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/satawat10/skills/agent-trade-kit-github-main) <br>
- [OKX](https://www.okx.com) <br>
- [Configuration Reference](references/config-reference.md) <br>
- [Notification Channels](references/notify-channels.md) <br>
- [Purchase Guide](references/purchase-guide.md) <br>
- [Scan Logic](references/scan-logic.md) <br>
- [Scheduler Setup](references/scheduler-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown notifications and guidance with JSON configuration and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce scheduled session, Telegram, or Lark notifications and local configuration/state updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
