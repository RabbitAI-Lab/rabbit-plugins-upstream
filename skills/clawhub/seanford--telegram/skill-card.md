## Description: <br>
OpenClaw skill for designing Telegram Bot API workflows and command-driven conversations using direct HTTPS requests (no SDKs). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design Telegram Bot API command flows, update routing, and operational checklists for bots that use direct HTTPS requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Telegram API requests may expose or misuse a real bot token if copied into logs, tickets, or shared transcripts. <br>
Mitigation: Treat bot tokens as secrets, avoid logging them, and review generated requests before using methods that send, edit, delete, or configure Telegram messages. <br>
Risk: Webhook or message-operation guidance may affect live Telegram chats if applied without review. <br>
Mitigation: Validate update payloads and chat context, use webhook secret token headers when possible, and test request payloads before production use. <br>


## Reference(s): <br>
- [Telegram Bot API Field Notes](references/telegram-bot-api.md) <br>
- [Telegram Command Playbook](references/telegram-commands-playbook.md) <br>
- [Telegram Request Templates](references/telegram-request-templates.md) <br>
- [Telegram Update Routing](references/telegram-update-routing.md) <br>
- [Telegram Bot API](https://core.telegram.org/bots/api) <br>
- [Telegram Bots FAQ](https://core.telegram.org/bots/faq) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown with HTTP request examples and JSON payload templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no executable code. Security evidence verdict: clean.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
