## Description: <br>
Full Mail enables agents to send email over SMTP and receive, search, read, mark, delete, and download attachments over IMAP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure email credentials and let an agent send messages, list and search inbox mail, read messages, download attachments, mark messages read, and delete messages through SMTP and IMAP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can permanently delete mailbox messages through its IMAP delete command. <br>
Mitigation: Avoid the delete command unless the account's recovery behavior is understood, and test with a low-risk mailbox before using it on important mail. <br>
Risk: The skill can write email attachments to disk, including attachments from untrusted senders. <br>
Mitigation: Download attachments only from trusted messages and scan downloaded files before opening them. <br>
Risk: The skill requires SMTP and IMAP credentials in the OpenClaw configuration. <br>
Mitigation: Use an app-specific password where supported, limit the mailbox scope, and protect the OpenClaw configuration file. <br>


## Reference(s): <br>
- [Full Mail on ClawHub](https://clawhub.ai/legionspace-hackathon/skills/full-mail) <br>
- [Configuration Guide](artifact/配置指南.md) <br>
- [Google App Passwords](https://myaccount.google.com/apppasswords) <br>
- [Google Account Security](https://myaccount.google.com/security) <br>
- [163 Mail](https://mail.163.com/) <br>
- [QQ Mail](https://mail.qq.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with command examples and plain-text CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can send outbound email, change mailbox state, and download attachments to ~/Downloads/email_attachments when invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
