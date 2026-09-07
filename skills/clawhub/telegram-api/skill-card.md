## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a connected Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a Telegram bot through Maton with managed authentication. It supports read/list workflows and user-approved write actions such as sending messages, managing bot commands, updating webhooks, and editing or deleting messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure from OAuth tokens, Maton API keys, or provider-issued tokens.

Mitigation: Prefer OAuth through the Maton CLI, do not print or persist credentials, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Unapproved writes can send messages, edit content, delete messages, change bot commands, or modify webhooks.

Mitigation: Default to read and list calls, then require explicit user approval with target identifiers, payload, and intended effect before POST, PUT, PATCH, or DELETE operations.

Risk: Ambiguous accounts or connections can send a request to the wrong Telegram bot.

Mitigation: List active connections first and specify the intended Maton profile and connection when more than one is available.

Risk: Telegram content, webhook payloads, or chat data may contain untrusted instructions or data.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and extract only fields needed for the user-approved task.

## Reference(s):

- [ClawHub Telegram Bot Skill](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and SDK or raw HTTP code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Telegram bot.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
