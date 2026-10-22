## Description:

Monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends alerts, and guides users through subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX users use this skill to monitor Earn opportunities, receive recurring notifications, and review subscription steps before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring scans run using existing OKX CLI authentication and create local configuration and scheduled jobs.

Mitigation: Review local files and scheduler entries during setup, and disable the schedule when monitoring is no longer wanted.

Risk: Opportunity details may be shared through a configured Telegram or Lark channel.

Mitigation: Confirm the notification destination and avoid sharing sensitive account details in alerts.

Risk: Subscriptions, transfers, and redemptions can change the user's financial position.

Mitigation: Review current terms and amounts, and explicitly confirm each transaction before execution.

## Reference(s):

- [Earn Hunter on ClawHub](https://clawhub.ai/okx-retail/skills/earn-hunter)
- [OKX](https://www.okx.com)
- [Scan logic](references/scan-logic.md)
- [Notification channels](references/notify-channels.md)
- [Purchase guide](references/purchase-guide.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown alerts and instructions with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Alerts can be delivered in a conversation or through configured Telegram or Lark notifications.]

## Skill Version(s):

1.4.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
