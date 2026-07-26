## Description: <br>
Automatically sends Telegram stickers and emoji reactions that match the mood and vibe of Telegram conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dandysuper](https://clawhub.ai/user/dandysuper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External ClawHub users can use this skill in Telegram chats to add mood-matched sticker and emoji reactions through a Telegram bot token and chat ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad autonomous authority to post Telegram stickers on the user's behalf. <br>
Mitigation: Enable it only for explicit opt-in chats, review its behavior before installing, and honor user opt-out requests immediately. <br>
Risk: The security evidence reports a code-injection risk in the helper script's emoji handling. <br>
Mitigation: Fix the emoji handling before broad use and avoid passing untrusted sticker-set or emoji values to the helper script. <br>
Risk: The Telegram bot token can authorize posting through the configured bot. <br>
Mitigation: Store TELEGRAM_BOT_TOKEN as a secret, limit where the bot is added, and rotate the token if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dandysuper/skills/tg-sticker-emoji-mood) <br>
- [Dandysuper publisher profile](https://clawhub.ai/user/dandysuper) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and Telegram API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID; may call the Telegram Bot API to send stickers.] <br>

## Skill Version(s): <br>
3.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
