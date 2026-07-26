## Description: <br>
Formats substantive Telegram replies into scannable HTML messages and sends them through a caller-specified Telegram bot account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmchow](https://clawhub.ai/user/tmchow) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill when a Telegram reply is longer than a short plain message or needs structure, such as lists, summaries, alerts, reports, or status updates. It formats the content for mobile-friendly Telegram delivery and sends it to the specified chat or thread. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Telegram delivery can expose sensitive content to the destination chat if prompts include secrets or private data. <br>
Mitigation: Send only content intended for Telegram and keep bot accounts, chat IDs, and topic IDs tightly scoped. <br>
Risk: Using the wrong bot account or chat target can deliver a message to an unintended recipient. <br>
Mitigation: Require callers to provide the bot account name explicitly and validate it against configured accounts before sending. <br>
Risk: Malformed HTML or overlong content can cause Telegram API delivery failures. <br>
Mitigation: Escape text content, split messages at section boundaries before the Telegram limit, and fall back to plain text when formatted delivery fails repeatedly. <br>


## Reference(s): <br>
- [Telegram Bot API endpoint](https://api.telegram.org) <br>
- [ClawHub skill page](https://clawhub.ai/tmchow/skills/telegram-compose) <br>
- [Publisher profile](https://clawhub.ai/user/tmchow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Telegram HTML message text plus a short success or error response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May split messages over 4,096 characters, retry selected Telegram API errors, and fall back to plain text if HTML formatting repeatedly fails.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
