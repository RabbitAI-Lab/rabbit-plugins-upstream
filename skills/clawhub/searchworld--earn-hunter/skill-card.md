## Description:

Automatically monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends push notifications, and guides subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Earn Hunter to configure recurring OKX Earn scans, receive opportunity notifications through session, Telegram, or Lark channels, and follow guided subscription steps when they choose to act.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create recurring background jobs, write local monitoring state, and send opportunity details to configured notification channels.

Mitigation: Confirm the scheduler mechanism, notification destination, smoke-test result, and uninstall path before enabling recurring monitoring.

Risk: The skill includes live financial subscription, redeem, transfer, and purchase guidance.

Mitigation: Proceed only after the exact product, amount, source account, and product risks are clear; require explicit user confirmation before financial actions.

Risk: Security evidence marks the release as suspicious because monitoring automation is combined with financial-action guidance.

Mitigation: Review the skill and scan findings before deployment, and keep purchase execution separate from monitoring unless the user intentionally hands off to the related earn skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/earn-hunter)
- [OKX homepage](https://www.okx.com)
- [Scan Logic](artifact/references/scan-logic.md)
- [Configuration Reference](artifact/references/config-reference.md)
- [Notification Channels](artifact/references/notify-channels.md)
- [Scheduler Setup](artifact/references/scheduler-setup.md)
- [Purchase Guide](artifact/references/purchase-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local state under ~/.okx/earn-hunter and scheduler entries when monitoring is activated.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
