## Description:

Monitors OKX Flash, Fixed, and Flexible Earn opportunities, sends alerts for matching offers, and guides users through subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT

## Use Case:

OKX users can monitor Flash Earn, Fixed Earn, and Flexible Earn offers, receive notifications when configured criteria match, and get guidance for subscribing to an offer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring scheduling can continue scans in the background.

Mitigation: Review the proposed schedule and pause or remove it using the documented platform-specific controls.

Risk: Activation stores resolved tool paths and the activation PATH in an environment snapshot used by scheduled scans.

Mitigation: Review the snapshot contents and keep the earn-hunter configuration directory access limited to the intended user.

Risk: Subscription guidance is adjacent to financial actions, and security guidance notes that the action boundary should be clear.

Mitigation: Review the asset, amount, term, and subscription details, and require explicit user direction before any purchase is executed.

## Reference(s):

- [Scheduler setup](artifact/references/scheduler-setup.md)
- [Notification channels](artifact/references/notify-channels.md)
- [Configuration reference](artifact/references/config-reference.md)
- [Purchase guide](artifact/references/purchase-guide.md)
- [Scan logic](artifact/references/scan-logic.md)
- [OKX](https://www.okx.com)
- [earn-hunter on ClawHub](https://clawhub.ai/okx-retail/skills/earn-hunter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown notifications and guidance, with JSON configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run recurring scans and send notifications; subscription execution uses a separate OKX skill when available.]

## Skill Version(s):

1.5.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
