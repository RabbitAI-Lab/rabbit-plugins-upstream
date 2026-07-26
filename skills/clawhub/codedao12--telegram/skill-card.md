## Description: <br>
OpenClaw skill for designing Telegram Bot API workflows and command-driven conversations using direct HTTPS requests (no SDKs). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to design command-first Telegram bots, plan webhook or polling update flows, and prepare safe direct HTTPS Bot API requests without an SDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Telegram bot tokens could be exposed through logs, shared prompts, or copied request examples. <br>
Mitigation: Keep bot tokens out of logs and shared prompts, and replace placeholders before sharing generated requests. <br>
Risk: Generated HTTPS requests can change live bot behavior, including webhook configuration and message edits or deletes. <br>
Mitigation: Review each request before running it against a production bot, and treat webhook, edit, and delete operations as live changes. <br>
Risk: High-volume update handling can trigger rate limits or duplicate processing. <br>
Mitigation: Use allowed_updates, idempotent handlers, processed update_id tracking, and backoff for 429 responses. <br>


## Reference(s): <br>
- [Telegram Bot API](https://core.telegram.org/bots/api) <br>
- [Telegram Bots FAQ](https://core.telegram.org/bots/faq) <br>
- [Telegram Bot API Field Notes](references/telegram-bot-api.md) <br>
- [Telegram Command Playbook](references/telegram-commands-playbook.md) <br>
- [Telegram Request Templates (HTTP)](references/telegram-request-templates.md) <br>
- [Telegram Update Routing](references/telegram-update-routing.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTPS request templates and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command designs, update routing plans, JSON request payloads, and token-handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
