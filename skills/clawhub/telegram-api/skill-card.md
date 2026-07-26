## Description: <br>
Telegram Bot API integration with managed authentication for sending messages, managing chats, handling updates, and interacting with users through a connected Telegram bot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate a connected Telegram bot through Maton-managed authentication, including sending content, reading bot updates, managing chats, and configuring commands or webhooks. It requires a valid Maton API key and user approval before write or delete operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exposed credentials could allow unauthorized access to Maton-managed Telegram bot operations. <br>
Mitigation: Keep MATON_API_KEY private, store it only in approved secret handling, and avoid printing or committing it. <br>
Risk: A request can affect the wrong bot, chat, message, webhook, command, or connection. <br>
Mitigation: Check the exact target and effect before execution, and include the Maton-Connection header when more than one bot is connected. <br>
Risk: Write, delete, webhook, command, or connection changes can alter Telegram bot behavior or user-visible content. <br>
Mitigation: Require explicit user approval before sends, deletes, webhook changes, command changes, or connection changes. <br>


## Reference(s): <br>
- [ClawHub Telegram Bot Skill](https://clawhub.ai/byungkyu/skills/telegram-api) <br>
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api) <br>
- [Telegram Bot API Available Methods](https://core.telegram.org/bots/api#available-methods) <br>
- [Telegram Bot API Formatting Options](https://core.telegram.org/bots/api#formatting-options) <br>
- [Telegram Bot API Inline Keyboards](https://core.telegram.org/bots/api#inlinekeyboardmarkup) <br>
- [Telegram Bot API Bot Commands](https://core.telegram.org/bots/api#setmycommands) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP, Python, JavaScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY; use Maton-Connection when more than one Telegram bot is connected.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
