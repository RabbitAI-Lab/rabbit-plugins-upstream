## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with the Telegram Bot API through Maton-managed authentication. It supports reading bot state, sending messages and media, managing chats and commands, handling updates, and requiring confirmation before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A file-download instruction points to a raw bot-token URL, which conflicts with managed authentication.

Mitigation: Prefer Maton-managed CLI or OAuth flows, and avoid raw bot-token download URLs unless the publisher provides a safe managed download path.

Risk: Telegram writes such as sending messages, changing webhooks, deleting messages, or changing connections can affect external users or bot state.

Mitigation: Default to read and list calls, specify the intended connection, and require explicit confirmation with the target and payload before writes.

Risk: Long-lived API keys and provider tokens can be exposed through environment variables, command lines, logs, or raw responses.

Mitigation: Prefer OAuth and operating-system credential storage, never print or persist credentials, and limit raw HTTP fallback to environments where the CLI cannot be installed.

Risk: Telegram content and webhook payloads may include untrusted user-controlled data.

Mitigation: Treat API responses as data, validate values before use, and do not execute or follow instructions contained in returned messages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Maton Homepage](https://maton.ai)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payloads, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, a Telegram Bot connection, and explicit confirmation before write operations.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
