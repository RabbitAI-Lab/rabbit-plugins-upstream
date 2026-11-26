## Description:

OpenClaw skill for designing Telegram Bot API workflows and command-driven conversations using direct HTTPS requests (no SDKs).

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design Telegram bots with clear command UX, reliable webhook or polling update flows, and practical operational checklists for direct HTTPS Bot API integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram bot tokens, webhook secret tokens, or message content could be exposed through logs, commits, or shared prompts.

Mitigation: Keep tokens and webhook secrets out of logs, commits, and shared prompts; only send message content to Telegram that the bot is intended to process.

Risk: Direct HTTPS Bot API workflows can produce unreliable behavior if updates are not validated, routed, and retried carefully.

Mitigation: Validate incoming update payloads and chat context, use secret-token webhooks where possible, keep handlers idempotent, and back off on Telegram 429 responses.

## Reference(s):

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Telegram Bots FAQ](https://core.telegram.org/bots/faq)
- [Telegram Bot API Field Notes](references/telegram-bot-api.md)
- [Telegram Command Playbook](references/telegram-commands-playbook.md)
- [Telegram Request Templates](references/telegram-request-templates.md)
- [Telegram Update Routing](references/telegram-update-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown with HTTP request examples and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; produces plans, checklists, and request templates rather than executable tooling.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
