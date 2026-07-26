## Description: <br>
Emailbox helps agents send, receive, search, forward, and schedule email through IMAP/SMTP for common mail providers, including attachments, HTML templates, and document-data email workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, developers, and operations teams use this skill to automate mailbox workflows such as sending reports, searching inboxes, forwarding messages, scheduling email delivery, and turning document or data outputs into email content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mailbox credentials can allow email read and send access. <br>
Mitigation: Use a dedicated mailbox or revocable app password, keep secrets out of shell history and logs, and revoke credentials when the workflow no longer needs them. <br>
Risk: Scheduled email queue files can contain full email contents on disk. <br>
Mitigation: Secure and regularly review or delete the local emailbox queue directory before and after scheduled workflows. <br>
Risk: Email content and attachments may include sensitive business, financial, legal, or personal information. <br>
Mitigation: Confirm recipients, attachments, and user authorization before sending or forwarding sensitive messages. <br>
Risk: Plaintext credential-file setup can persist secrets beyond the active session. <br>
Mitigation: Prefer session-only environment variables or a system credential manager; avoid plaintext credential files unless access is tightly restricted. <br>


## Reference(s): <br>
- [Emailbox ClawHub Skill Page](https://clawhub.ai/tobewin/skills/emailbox) <br>
- [Document Integration](references/integrations.md) <br>
- [Email Provider Configuration](references/providers.md) <br>
- [HTML Email Templates](references/templates.md) <br>
- [Microsoft Account Security](https://account.microsoft.com/security) <br>
- [Google Account Security](https://myaccount.google.com/security) <br>
- [Google App Passwords](https://myaccount.google.com/apppasswords) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated email body, attachment, and schedule-queue files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local Python scripts and provider-specific IMAP/SMTP credentials supplied through environment variables.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
