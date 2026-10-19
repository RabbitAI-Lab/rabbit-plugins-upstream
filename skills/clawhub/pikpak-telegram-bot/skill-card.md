## Description:

Helps users control PikPak through an authorized Telegram bot to submit links, check tasks, and list root files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can configure an authorized Telegram bot to submit links to PikPak and check task status or root files remotely. Deployment and outbound messages require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bot credentials and the PikPak CLI session grant remote account access.

Mitigation: Keep credentials out of chat and logs, use a private state directory, and configure strict chat and user whitelists.

Risk: Untrusted bot executables or Telegram API endpoints could expose credentials or redirect requests.

Mitigation: Do not point PIKPAK_BIN or TG_API_BASE at untrusted programs or services.

Risk: An uncertain link submission may already have created a remote task.

Mitigation: Check the task in PikPak before attempting a manual retry; do not automatically replay unknown submissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-telegram-bot)
- [Upstream design notes](artifact/references/upstream-design.md)
- [Telegram Bot API: getUpdates](https://core.telegram.org/bots/api#getupdates)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit authorization before deployment or outbound messages.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
