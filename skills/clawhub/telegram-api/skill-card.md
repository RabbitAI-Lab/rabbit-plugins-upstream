## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a connected Telegram bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make Telegram Bot API calls through the Maton gateway, including reading bot state, sending messages, managing chats, configuring bot commands, and handling updates with user-confirmed write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found a file-download instruction that conflicts with the managed-auth model by directing use of a bot token in a URL.

Mitigation: Review the file-download section before use; avoid constructing, printing, pasting, logging, or storing Telegram bot-token URLs, and prefer gateway-mediated access where possible.

Risk: Telegram actions such as sending messages, setting webhooks, deleting content, or changing bot profile details can affect external users or public behavior.

Mitigation: Confirm the target, payload, and intended effect with the user before any message, webhook, delete, profile-changing, or other POST, PUT, PATCH, or DELETE operation.

Risk: Multiple Maton profiles or Telegram connections can cause actions to run against the wrong bot account.

Mitigation: List and verify active connections first, then specify the intended connection and profile for task-relevant calls.

## Reference(s):

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboard Markup](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Set My Commands](https://core.telegram.org/bots/api#setmycommands)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/telegram-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with shell, JSON, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes managed-auth workflow guidance, read-first posture, and explicit approval requirements for connection creation and write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
