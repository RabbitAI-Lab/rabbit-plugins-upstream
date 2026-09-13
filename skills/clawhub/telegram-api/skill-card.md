## Description:

Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and building approved bot automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to let an agent work with Telegram bots through Maton-managed authentication. It supports bot messaging, chat administration, update handling, webhook setup, hosted functions, and scheduled or event-driven automation when the user explicitly approves those actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the connection lets Maton operate the Telegram bot within the bot token's allowed capabilities.

Mitigation: Connect only the bot needed for the task, prefer read-only checks first, and revoke unused connections promptly.

Risk: Sends, edits, deletes, forwards, and bot command changes can affect chats or disclose message content.

Mitigation: Require explicit user approval for each write, including the target chat, resource identifiers, payload, and intended effect.

Risk: Webhooks, triggers, hosted functions, and destinations can create persistent forwarding or repeated actions until removed.

Mitigation: Approve automation separately, use user-provided destinations only, narrow event scopes, inspect existing webhook state first, and remove automation when no longer needed.

Risk: Telegram messages, webhook payloads, and trigger events may contain sensitive or adversarial content.

Mitigation: Treat external data as untrusted, do not execute or interpolate it into commands, and avoid logging full raw responses unless the user explicitly asks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Maton homepage](https://maton.ai)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods)
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options)
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for connection creation, writes, deletes, webhooks, hosted functions, triggers, and destinations.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
