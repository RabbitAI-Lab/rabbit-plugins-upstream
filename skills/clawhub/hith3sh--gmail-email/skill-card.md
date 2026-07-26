## Description: <br>
Read, search, draft, reply to, and organize Gmail from chat through the Gmail API using ClawLink-connected tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hith3sh](https://clawhub.ai/user/hith3sh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent search, read, draft, send, reply to, forward, label, archive, trash, and inspect Gmail messages after the user's Gmail account is connected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through email write or destructive actions, including sending, forwarding, labeling, archiving, trashing, or deleting messages. <br>
Mitigation: Preview write actions and confirm recipients, subject, body, labels, and destructive intent with the user before execution. <br>
Risk: The skill operates on a connected Gmail mailbox and may expose sensitive message, attachment, contact, or account information during use. <br>
Mitigation: Review the installed instructions and requested account permissions before use, and keep access scoped to the intended connected Google account. <br>


## Reference(s): <br>
- [Gmail API Documentation](https://developers.google.com/gmail/api) <br>
- [Gmail API Reference](https://developers.google.com/gmail/api/reference/rest) <br>
- [Gmail Query Syntax](https://support.google.com/mail/answer/7190) <br>
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=gmail-email) <br>
- [ClawLink Docs](https://docs.claw-link.dev/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON tool-call parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a connected Gmail account through ClawLink; write and destructive operations require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
