## Description: <br>
Build and manage Telegram bots via the Telegram Bot API, including bot setup, messaging, webhooks, group and channel operations, and chat moderation commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sebastian-buitrag0](https://clawhub.ai/user/sebastian-buitrag0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and bot operators use this skill to configure Telegram bot credentials, call Telegram Bot API endpoints, send messages and media, manage updates and webhooks, and administer chats, groups, or channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Telegram bot tokens can grant control over bots if exposed in logs, terminal history, or shared command output. <br>
Mitigation: Store TELEGRAM_BOT_TOKEN as a secret, avoid sharing expanded token URLs, and rotate the token promptly if it is exposed. <br>
Risk: Bot update logs and message handling can reveal chat data, forwarded messages, user identifiers, or location information. <br>
Mitigation: Limit collection and sharing of update output, review logs for sensitive chat data, and handle user data according to the deployment's privacy requirements. <br>
Risk: Chat administration commands such as banning, unbanning, deleting, pinning, or forwarding messages can affect real users and channels. <br>
Mitigation: Use moderation commands only on bots and chats you control, verify chat and user IDs before execution, and test actions in a controlled chat first. <br>


## Reference(s): <br>
- [ClawHub Telegram Bot Builder listing](https://clawhub.ai/sebastian-buitrag0/skills/telegram-bot) <br>
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api) <br>
- [BotFather Commands](https://core.telegram.org/bots#botfather) <br>
- [Telegram Bot API Changelog](https://core.telegram.org/bots/api-changelog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash curl commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a TELEGRAM_BOT_TOKEN environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
