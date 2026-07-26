## Description: <br>
Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fianabates1](https://clawhub.ai/user/fianabates1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill when the user explicitly asks to send WhatsApp messages to third parties or search and sync WhatsApp history through the wacli CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send WhatsApp messages or files to third-party recipients through the user's account. <br>
Mitigation: Require an explicit recipient and message or file from the user, then confirm the recipient and content before sending. <br>
Risk: Synced WhatsApp history may be stored locally in ~/.wacli and can contain sensitive personal information. <br>
Mitigation: Treat the wacli store directory as sensitive and only sync or search history when the user explicitly requests it. <br>
Risk: Ambiguous recipient names, phone numbers, group IDs, or message text could cause unintended disclosure. <br>
Mitigation: Ask a clarifying question whenever the recipient, destination, attachment, or message content is ambiguous. <br>


## Reference(s): <br>
- [wacli homepage](https://wacli.sh) <br>
- [ClawHub skill page](https://clawhub.ai/fianabates1/skills/test-wa) <br>
- [wacli Go module](https://github.com/steipete/wacli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and confirmation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use JSON-formatted CLI output when parsing wacli responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
