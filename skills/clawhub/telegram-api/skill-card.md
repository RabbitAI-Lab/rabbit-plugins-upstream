## Description:

Guides an agent in using the Telegram Bot API to read updates, manage chats, send messages, and configure bot automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and bot operators use this skill to inspect Telegram bot activity, respond to chats, manage bot settings, and set up approved webhooks or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending, editing, or deleting bot messages can affect real chats.

Mitigation: Start with read-only calls and confirm each write with the user.

Risk: Webhooks and automations can persistently forward updates to a destination.

Mitigation: Confirm each webhook destination and automation, and keep trigger scopes narrow.

Risk: Raw API-key mode exposes a long-lived credential to the calling environment.

Mitigation: Prefer CLI-managed authentication; use raw API-key mode only when the CLI cannot be used.

## Reference(s):

- [Telegram Bot skill release](https://clawhub.ai/byungkyu/skills/telegram-api)
- [Maton homepage](https://maton.ai)
- [Telegram Bot API documentation](https://core.telegram.org/bots/api)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide approved Telegram API actions and persistent automations.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
