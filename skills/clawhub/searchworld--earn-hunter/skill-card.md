## Description:

Earn Hunter monitors OKX Flash Earn, Fixed Earn, and Flexible Earn opportunities, sends push notifications, and guides users through subscription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor OKX Earn opportunities, configure scan thresholds, receive Telegram, Lark, or session notifications, and get guided next steps for subscription decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs persistent account-aware scans and may guide high-impact financial actions.

Mitigation: Review before installing, use a minimally permissioned OKX profile, and confirm any subscription, redeem, purchase, or scheduler action before use.

Risk: Dependent skills or CLI installation may change if versions are not pinned.

Mitigation: Pin the OKX CLI and dependent skill versions used in the environment before relying on scheduled monitoring.

Risk: Scheduled scans and notification delivery depend on local scheduler, shell, and path configuration.

Mitigation: Confirm the scheduler entry or cron job and run the activation smoke tests, including the minimal cron environment check.

Risk: Telegram or Lark notifications use local shell commands and may expose bot or webhook credentials in the local environment.

Mitigation: Use Telegram and Lark credentials only in environments where local shell command handling and log access are acceptable.

## Reference(s):

- [Configuration Reference](artifact/references/config-reference.md)
- [Scan Logic](artifact/references/scan-logic.md)
- [Notification Channels](artifact/references/notify-channels.md)
- [Scheduler Setup](artifact/references/scheduler-setup.md)
- [Purchase Guide](artifact/references/purchase-guide.md)
- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/earn-hunter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update local config, state, scheduler, and notification settings during activation.]

## Skill Version(s):

1.4.7 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
