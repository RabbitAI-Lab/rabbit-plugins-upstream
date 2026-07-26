## Description: <br>
Rename Telegram forum topics and optionally change their icons via the Telegram Bot API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwjjhh1995](https://clawhub.ai/user/wwjjhh1995) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, moderators, and operators managing Telegram forum chats use this skill to rename existing topics and optionally apply a matching forum-topic icon through the Telegram Bot API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Telegram bot token can authorize real topic-name and icon changes in chats where the bot has permission. <br>
Mitigation: Use a dedicated bot token with minimal access and keep the token out of logs and shared files. <br>
Risk: Supplying the wrong chat_id or thread_id can rename the wrong Telegram forum topic. <br>
Mitigation: Verify the chat_id and thread_id before running the script. <br>


## Reference(s): <br>
- [Telegram Topic Icons Reference](artifact/references/icons.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/wwjjhh1995/skills/telegram-topic-rename) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TELEGRAM_BOT_TOKEN and caller-supplied chat_id, thread_id, and topic name; optional icon input may be an emoji shortcut or custom emoji ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
