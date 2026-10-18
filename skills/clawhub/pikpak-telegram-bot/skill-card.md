## Description:

Helps authorized Telegram users save links to PikPak and check tasks or root-directory items through a locally run bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and operators can configure a Telegram bot to submit magnet or web links and inspect download tasks and recent root-directory items. Deployment and live account actions require explicit user authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed bot token or an untrusted group could allow unwanted access to PikPak actions or reveal query results.

Mitigation: Configure credentials privately, restrict chat and group-sender allowlists, and prefer private chats for sensitive account information.

Risk: A timed-out or unconfirmed save request might already have reached PikPak.

Mitigation: Check the PikPak account before retrying; keep the private persistent state records instead of automatically replaying unknown submissions.

Risk: Using the disclosed registration referral code may reward the sharer.

Mitigation: Let the user opt in explicitly; the skill can be used without the referral code.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-telegram-bot)
- [Upstream design references](artifact/references/upstream-design.md)
- [Telegram Bot API: getUpdates](https://core.telegram.org/bots/api#getupdates)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and Telegram text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task and directory results may be truncated; an unconfirmed submission is not reported as a completed download.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
