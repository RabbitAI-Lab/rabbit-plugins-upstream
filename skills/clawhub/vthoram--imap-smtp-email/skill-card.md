## Description: <br>
Read, search, manage, and send email through IMAP and SMTP using a configured email account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vthoram](https://clawhub.ai/user/vthoram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect inbox state, search and fetch messages, download attachments, update read state, and send SMTP email from configured accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, search, modify read state, download attachments, and send mail for configured accounts. <br>
Mitigation: Use app-specific credentials with the narrowest available mailbox access and review each send, download, and mark-read action before execution. <br>
Risk: Credentials in the .env file can provide ongoing mailbox access if exposed. <br>
Mitigation: Restrict the .env file to the current user, keep it out of version control and shared workspaces, and rotate credentials if exposure is suspected. <br>
Risk: Disabling certificate verification for self-signed servers weakens TLS protections. <br>
Mitigation: Keep IMAP_REJECT_UNAUTHORIZED and SMTP_REJECT_UNAUTHORIZED enabled unless the mail server is fully trusted. <br>
Risk: Security evidence advises updating or replacing vulnerable dependencies before important mailbox use. <br>
Mitigation: Update dependencies and re-scan the skill before using it with sensitive or important email accounts. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/vthoram/skills/imap-smtp-email) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read mailbox content, download attachments, mark messages read or unread, and send email through configured IMAP and SMTP credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
