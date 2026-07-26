## Description: <br>
Search chats, list/read messages, and send messages via Beeper Desktop using the beeper-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[foeken](https://clawhub.ai/user/foeken) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to operate Beeper Desktop through the beeper-cli, including finding chats, reading or searching messages, and sending or editing messages when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Beeper chats and search message history. <br>
Mitigation: Use it deliberately and quote only the message content needed for the task. <br>
Risk: The skill can perform state-changing messaging actions such as sending, editing, archiving, creating chats, uploading files, downloading files, and deleting reminders. <br>
Mitigation: Require explicit review of recipients, chat IDs, message text, and file paths before running state-changing commands. <br>
Risk: The Beeper access token grants access to private chat data. <br>
Mitigation: Keep BEEPER_ACCESS_TOKEN private and store it securely. <br>
Risk: Installing beeper-cli with @latest can pull unreviewed changes from the third-party CLI. <br>
Mitigation: Prefer a trusted, pinned release when installing the beeper-cli dependency. <br>


## Reference(s): <br>
- [Beeper CLI on ClawHub](https://clawhub.ai/foeken/skills/beeper-cli) <br>
- [beeper-cli](https://github.com/foeken/beeper-cli) <br>
- [beeper-cli releases](https://github.com/foeken/beeper-cli/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include beeper-cli commands that read chats, search messages, send or edit messages, manage chats, and upload or download attachments.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
