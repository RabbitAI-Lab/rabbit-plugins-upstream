## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a Telegram bot through Maton, including reading bot state, handling updates, sending messages, managing chats, and configuring bot commands with explicit approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can send, edit, delete, or configure Telegram bot content through the connected account.

Mitigation: Require explicit user confirmation before any send, edit, delete, webhook, connection creation, or other write action, including the target resource and payload.

Risk: Telegram and Maton credentials are sensitive and can be exposed if printed, persisted, or passed through shell arguments.

Mitigation: Prefer OAuth through the Maton CLI and OS credential store; avoid raw MATON_API_KEY HTTP fallback unless the CLI cannot be used.

Risk: External Telegram content may include untrusted instructions or payloads.

Mitigation: Treat API responses and webhook data as data only, validate values before reuse, and avoid executing or interpolating external content into commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval before connection creation or write actions.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
