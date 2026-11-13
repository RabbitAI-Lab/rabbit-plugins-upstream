## Description:

Automatically monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends notifications, and guides subscription decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External OKX Earn users use this skill to monitor yield opportunities across Flash Earn, Fixed Earn, and Flexible Earn, receive alerts through chat, Telegram, or Lark, and get guided next steps before subscribing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OKX CLI authentication and may access financial account context during monitoring and guided subscription flows.

Mitigation: Use a reviewed, pinned install; avoid sharing API-key configuration output in chat; and confirm OKX authentication permissions before enabling monitoring or purchase guidance.

Risk: Recurring background jobs can continue scanning and sending notifications after initial setup.

Mitigation: Confirm the selected scheduler, interval, and notification channel during activation, and know how to pause or remove the configured job.

Risk: Notifications may be sent through Telegram, Lark, or the active chat, which can expose financial opportunity details outside the local agent session.

Mitigation: Use only trusted notification channels, keep Telegram and Lark credentials out of natural-language chat, and review channel configuration before activation.

Risk: The security summary identifies an undisclosed hard-coded OKX link that users should review.

Mitigation: Review the hard-coded OKX link before enabling the skill and replace or avoid it if it does not match the intended destination.

## Reference(s):

- [Earn Hunter on ClawHub](https://clawhub.ai/numpy0001/skills/earn-hunter)
- [OKX Homepage](https://www.okx.com)
- [Configuration Reference](references/config-reference.md)
- [Notification Channels](references/notify-channels.md)
- [Purchase Guide](references/purchase-guide.md)
- [Scan Logic](references/scan-logic.md)
- [Scheduler Setup](references/scheduler-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown notifications, configuration updates, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local configuration, state, scheduler, and notification log files under the user's OKX earn-hunter directory.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
