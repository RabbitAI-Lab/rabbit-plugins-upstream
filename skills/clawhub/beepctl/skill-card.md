## Description: <br>
Use when sending messages, searching chats, or managing conversations across messaging platforms via the Beeper Desktop API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blqke](https://clawhub.ai/user/blqke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users use this skill to let an agent operate the beepctl CLI for Beeper-connected accounts, including listing accounts and chats, searching messages, sending text messages, managing aliases and reminders, archiving chats, focusing Beeper, and downloading attachments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access chats, handle API tokens, send messages, and save attachments through Beeper-connected accounts. <br>
Mitigation: Install only if the external beepctl npm package is trusted, keep tokens out of transcripts and shell history, and save attachments only to deliberately chosen locations. <br>
Risk: The agent could send or modify messages or conversation state for the wrong recipient or chat. <br>
Mitigation: Require explicit user confirmation before sending messages or performing account-changing actions, and verify recipients, chat IDs, and aliases before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/blqke/skills/beepctl) <br>
- [beepctl GitHub repository](https://github.com/blqke/beepctl) <br>
- [Beeper Desktop API documentation](https://developers.beeper.com/desktop-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external beepctl binary and access to Beeper-connected accounts.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
