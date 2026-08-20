## Description:

Automatically monitors OKX Flash Earn, Fixed Earn and Flexible Earn opportunities, sends push notifications, and guides subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to monitor OKX Earn opportunities across Flash Earn, Fixed Earn, and Flexible Earn, receive alerts, configure scan thresholds, and get guided subscription steps. It is intended for ongoing monitoring with explicit user confirmation before asset-moving actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has ongoing scheduler access, local OKX Earn state, and optional Telegram or Lark notification delivery.

Mitigation: Install only when those access patterns are acceptable, review scheduler and notification configuration during setup, and keep credentials in environment variables or platform configuration rather than chat.

Risk: The skill guides users toward real asset-moving purchase, transfer, and redeem workflows from a monitoring context.

Mitigation: Confirm asset, amount, term, source account, and destination before any transfer, redeem, or fixed-purchase command is run, and prefer the dedicated transaction skill or the OKX app for execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/earn-hunter)
- [OKX](https://www.okx.com)
- [Purchase Guide](references/purchase-guide.md)
- [Scan Logic](references/scan-logic.md)
- [Scheduler Setup](references/scheduler-setup.md)
- [Notification Channels](references/notify-channels.md)
- [Configuration Reference](references/config-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and notification templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces monitoring alerts, setup guidance, configuration edits, scan output summaries, and confirmation-oriented purchase guidance.]

## Skill Version(s):

1.4.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
