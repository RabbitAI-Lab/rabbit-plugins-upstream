## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to the Telegram Bot API through Maton, inspect bot and chat state, send or edit messages, manage commands and webhooks, and retrieve updates. The skill is intended for workflows where credentials stay managed and sensitive actions are confirmed with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram bot actions can send, edit, delete, or forward messages and can affect external chats.

Mitigation: Default to read-only calls, verify the target account and chat identifiers, and require explicit user confirmation before any send, edit, delete, connection, or other write action.

Risk: Webhook configuration can continuously forward future Telegram updates, including message content and sender metadata, to the configured URL.

Mitigation: Check current webhook state first, accept webhook URLs only from the user, explain the ongoing data flow, narrow allowed update types, and confirm before setting or replacing a webhook.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is required, never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Telegram file download URLs embed the bot token when constructed directly from file_path values.

Mitigation: Do not construct token-bearing Telegram file URLs; use getFile only to return file_path metadata and ask the user how downloads should be authorized when bytes are required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for Maton CLI or raw HTTPS use; it does not expose Telegram bot tokens.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
