## Description:

Earn Hunter monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends opportunity notifications, and guides users through subscription flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to monitor OKX Earn products, receive alerts for matching opportunities, adjust monitoring preferences, and get guided support for subscription decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent scheduled jobs for recurring monitoring.

Mitigation: Review and explicitly confirm scheduler setup, keep the interval intentional, and use the documented pause or uninstall steps to remove scheduled jobs exactly.

Risk: The skill uses the OKX CLI login context for live account data and includes high-impact subscription guidance.

Mitigation: Review the purchase guide before subscription flows, require explicit user confirmation before any purchase step, and recheck offer availability before execution.

Risk: The skill writes configuration, state, logs, and scan scripts under ~/.okx/earn-hunter.

Mitigation: Use restrictive file permissions, review generated configuration before unattended operation, and remove local state during uninstall if monitoring is no longer needed.

Risk: The skill can send opportunity notifications through Telegram or Lark.

Mitigation: Store Telegram credentials in environment variables, validate Lark webhook URLs, and confirm test delivery before relying on unattended notifications.

## Reference(s):

- [Earn Hunter ClawHub Listing](https://clawhub.ai/searchworld/skills/earn-hunter)
- [OKX](https://www.okx.com)
- [Configuration Reference](references/config-reference.md)
- [Notification Channels](references/notify-channels.md)
- [Purchase Guide](references/purchase-guide.md)
- [Scan Logic](references/scan-logic.md)
- [Scheduler Setup](references/scheduler-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces monitoring setup steps, scan results, notification messages, subscription guidance, and local configuration updates.]

## Skill Version(s):

1.4.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
