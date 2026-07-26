## Description: <br>
Manage and configure Telegram bots for OpenClaw. Use when setting up Telegram integrations, troubleshooting bot connectivity, configuring bot tokens, or managing Telegram channel/webhook settings. Handles bot registration, token validation, and network connectivity checks for api.telegram.org. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[362224222](https://clawhub.ai/user/362224222) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to set up, test, and troubleshoot Telegram bot integrations for OpenClaw, including token configuration, connectivity checks, and webhook or polling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Telegram bot tokens in flows that can expose secrets through command-line arguments, shell history, logs, shared terminals, screenshots, or local configuration files. <br>
Mitigation: Use a dedicated Telegram bot token, prefer environment or secure config storage over command-line arguments, restrict permissions on OpenClaw config and backup files, and rotate any token that may have been exposed. <br>
Risk: The setup script can modify local OpenClaw configuration and restart the OpenClaw gateway. <br>
Mitigation: Review scripts before execution, run them in the intended OpenClaw environment, confirm backups are created, and be prepared to restore configuration or restart the gateway manually. <br>
Risk: The server security evidence says not to assume this is an official OpenClaw publisher package solely from the author field. <br>
Mitigation: Treat the release as a third-party ClawHub package from publisher handle 362224222 and validate it against local operational and security requirements before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/362224222/skills/telegram-bot-manager) <br>
- [OpenClaw Telegram Configuration Guide](references/OPENCLAW_CONFIG.md) <br>
- [Telegram Webhook Setup Guide](references/WEBHOOK_SETUP.md) <br>
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api) <br>
- [BotFather Documentation](https://core.telegram.org/bots#6-botfather) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational guidance for OpenClaw configuration, Telegram API checks, webhook setup, and local helper scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact/metadata.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
