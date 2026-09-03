## Description:

Companion plugin for ClawVision: add PDF, OG images, and Telegram sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this companion plugin after ClawVision has generated a summary card to export a multi-page PDF, create a 1200x630 OG image, or send the generated summary image and caption to Telegram.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram sharing can send generated summary content outside the local environment.

Mitigation: Use Telegram delivery only after explicit user confirmation and only provide a bot token and chat ID for the intended chat or channel.

Risk: Telegram bot tokens are sensitive credentials.

Mitigation: Keep bot tokens out of chat and logs, and provide them only at execution time when Telegram sharing is intentionally requested.

Risk: Dependency exposure may change over time for Playwright, Pillow, reportlab, and python-telegram-bot.

Mitigation: Install with a reviewed lockfile or pinned patched dependency versions before deployment.

## Reference(s):

- [ClawVision Plus README](references/README.md)
- [ClawVision project](https://github.com/monaxamo/clawvision)
- [BotFather](https://t.me/BotFather)
- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-plus)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, API Calls]

**Output Format:** [JSON status output plus generated PDF, PNG, and optional Telegram message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an existing ClawVision summary JSON and rendered HTML card; Telegram delivery requires an explicit chat ID and bot token.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
