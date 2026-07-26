## Description: <br>
Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rafay0313](https://clawhub.ai/user/rafay0313) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill when the user explicitly asks to message someone else on WhatsApp or search, sync, or backfill WhatsApp history through the wacli CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could send a WhatsApp message or file to the wrong recipient, or send unintended content. <br>
Mitigation: Require an explicit recipient and message or file path, then confirm the exact recipient and content before sending. <br>
Risk: WhatsApp sync, search, and backfill can expose private chat history. <br>
Mitigation: Use history operations only after an explicit user request and keep searches or backfills scoped to the requested chat and time range when possible. <br>
Risk: The local wacli store may contain WhatsApp session or chat data. <br>
Mitigation: Treat the wacli store as private user data and avoid exposing or sharing its contents. <br>


## Reference(s): <br>
- [wacli homepage](https://wacli.sh) <br>
- [ClawHub skill listing](https://clawhub.ai/rafay0313/skills/tt) <br>
- [wacli Go install module](https://github.com/steipete/wacli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use JSON CLI output when parsing wacli responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
