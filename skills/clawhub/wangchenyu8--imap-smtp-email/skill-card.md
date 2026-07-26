## Description: <br>
Read and send email via IMAP/SMTP. Check for new/unread messages, fetch content, search mailboxes, mark as read/unread, and send emails with attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangchenyu8](https://clawhub.ai/user/wangchenyu8) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure one or more email accounts, inspect mailbox state, retrieve messages and attachments, search mailboxes, update read state, and send messages through IMAP and SMTP providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires email credentials and can read mailbox contents or send email through the configured account. <br>
Mitigation: Use a dedicated app password or throwaway mailbox where possible, and install only when that account access is intended. <br>
Risk: Email sending and attachment handling can expose local files or send messages to unintended recipients. <br>
Mitigation: Keep allowed read and write directories narrow, and verify recipients, message content, and attachment paths before sending. <br>
Risk: Setup can migrate credentials from a legacy .env file. <br>
Mitigation: Review the setup script and avoid migrating from any untrusted legacy configuration file. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangchenyu8/skills/imap-smtp-email) <br>
- [Publisher profile](https://clawhub.ai/user/wangchenyu8) <br>
- [Google App Passwords](https://myaccount.google.com/apppasswords) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration examples, and command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read mailbox content, send email, and read or write local files only as directed by the configured command and allowed directories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
