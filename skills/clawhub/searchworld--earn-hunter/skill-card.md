## Description:

Automatically monitors OKX Flash Earn, Fixed Earn and Flexible Earn opportunities, sends push notifications, and guides subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Earn Hunter to monitor OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, configure thresholds and scan schedules, receive Telegram, Lark, or session alerts, and get subscription guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent background automation can continue scanning and sending alerts after activation.

Mitigation: Before activation, confirm the notification destination and scheduler, and review any cron, OpenClaw cron, or platform scheduler entry the skill creates.

Risk: The skill includes high-impact financial transaction guidance and fallback purchase commands.

Mitigation: Before any subscription action, recheck the product, amount, term, lock-up, and final confirmation yourself; avoid fallback commands unless each parameter has been verified.

Risk: Telegram or Lark notifications can expose opportunity details to the configured destination.

Mitigation: Confirm the intended channel before enabling alerts, keep Telegram credentials in environment variables, and verify Lark webhook URLs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/earn-hunter)
- [OKX homepage](https://www.okx.com)
- [Configuration Reference](references/config-reference.md)
- [Notification Channels](references/notify-channels.md)
- [Purchase Guide](references/purchase-guide.md)
- [Scan Logic](references/scan-logic.md)
- [Scheduler Setup](references/scheduler-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown notifications and guidance with inline shell commands and JSON configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent local configuration, state, scheduler, and notification files under the user's OKX Earn Hunter state directory.]

## Skill Version(s):

1.4.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
