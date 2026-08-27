## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a Telegram bot through Maton-managed authentication, including reading bot state, sending messages, handling updates, managing chats, and configuring bot commands or webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a Telegram bot and perform write actions such as sending messages or changing webhooks and bot commands.

Mitigation: Review the target connection before use and require explicit confirmation before sending messages or changing webhooks or commands.

Risk: Long-lived API keys can be exposed if used instead of OAuth.

Mitigation: Prefer Maton OAuth authentication and avoid printing, storing, or passing API keys in command-line arguments.

Risk: Actions may target the wrong Telegram bot or Maton account when multiple connections or profiles exist.

Mitigation: Verify the intended connection before use and specify the connection or profile when ambiguity exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Maton](https://maton.ai)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Telegram bot account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
