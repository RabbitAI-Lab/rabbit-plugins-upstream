## Description:

Earn Hunter monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends notifications, and guides subscription flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure scheduled OKX Earn opportunity monitoring, receive Telegram, Lark, or session alerts, and review guided subscription steps before taking financial action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent scheduled monitoring runs under the user's account context.

Mitigation: Install only after reviewing the scheduler setup, inspect ~/.okx/earn-hunter/env.snapshot, and confirm the configured cron, LaunchAgent, or OpenClaw cron job matches the intended interval and notification channel.

Risk: Financial actions such as redeem, transfer, or purchase can have high impact if executed with broad account permissions.

Mitigation: Use a dedicated low-privilege OKX profile or API key where possible, avoid withdrawal permission unless transfer flows are intended, and require explicit user confirmation before redeem, transfer, or purchase commands.

Risk: Guided purchase flows can become stale if an Earn product sells out or changes before execution.

Mitigation: Recheck product availability immediately before final confirmation and abort if the target product is sold out or no longer listed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/earn-hunter)
- [OKX](https://www.okx.com)
- [Configuration Reference](references/config-reference.md)
- [Notification Channels](references/notify-channels.md)
- [Purchase Guide](references/purchase-guide.md)
- [Scan Logic](references/scan-logic.md)
- [Scheduler Setup](references/scheduler-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces scheduled-monitoring setup guidance, notification text, and purchase-review guidance; it does not produce binary artifacts.]

## Skill Version(s):

1.4.8 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
