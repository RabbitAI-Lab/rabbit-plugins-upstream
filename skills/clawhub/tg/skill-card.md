## Description: <br>
Telegram CLI for reading, searching, and sending messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to authenticate a Telegram CLI, read inbox and chat data, search contacts or groups, and send or reply to messages from the authenticated account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private Telegram messages, contacts, groups, and locally synced chat data from the authenticated account. <br>
Mitigation: Authenticate only the Telegram account intended for agent access, limit broad search or sync commands for sensitive chats, and review returned data before sharing it further. <br>
Risk: The skill can send or reply to Telegram messages from the authenticated account. <br>
Mitigation: Confirm the recipient, chat, message ID, and message text before running send or reply commands. <br>
Risk: The release depends on the third-party @cyberdrk/tg package. <br>
Mitigation: Install only if you trust the package publisher or have reviewed the package source and release artifacts. <br>


## Reference(s): <br>
- [Telegram application credentials](https://my.telegram.org/apps) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI commands may return plain text, Markdown, or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can read or search Telegram account data and can send or reply to messages from the authenticated account.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
