## Description:

Helps users run a self-hosted Telegram bot to save links to PikPak and check tasks and files remotely.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can set up a local Telegram bot to send links or magnets to PikPak and check transfer status and file listings from Telegram.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized Telegram chats could add PikPak tasks or view task and file names.

Mitigation: Restrict PIKPAK_ALLOWED_CHAT_IDS to trusted chats and keep the bot token private.

Risk: Task and file names can appear in Telegram replies or local logs.

Mitigation: Use private chats and avoid exposing bot logs publicly.

Risk: Custom Telegram API endpoints or PikPak executables may be untrusted.

Mitigation: Only override TG_API_BASE or PIKPAK_BIN when you trust the service or binary.

## Reference(s):

- [PikPak Telegram Bot on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-telegram-bot)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown setup guidance and Telegram text replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a local bot script; replies can include task IDs, progress, and file names.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
