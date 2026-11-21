## Description:

Read and send email via IMAP/SMTP. Check for new/unread messages, fetch content, search mailboxes, mark as read/unread, and send emails with attachments. Supports multiple accounts. Works with any IMAP/SMTP server including Gmail, Outlook, 163.com, vip.163.com, 126.com, vip.126.com, 188.com, and vip.188.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troioi-vn](https://clawhub.ai/user/troioi-vn)

### License/Terms of Use:

MIT-0

## Use Case:

People with configured IMAP/SMTP accounts use this skill to read, search, organize, and send email, including messages with attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create mailboxes and copy or move messages, which changes mailbox contents.

Mitigation: Use these commands only when requested, and confirm the source and destination mailboxes before moving messages.

Risk: The setup guidance allows disabling TLS certificate verification for servers with self-signed certificates.

Mitigation: Keep certificate verification enabled unless the server certificate has been independently checked and the exception is necessary.

Risk: The security scan was incomplete, so it does not establish that unexamined portions are safe.

Mitigation: Review the skill and its permissions before configuring it with mailbox credentials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/troioi-vn/skills/imap-smtp-email-maddy-fix)
- [Google Account App Passwords](https://myaccount.google.com/apppasswords)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON command results with email content and metadata; downloaded attachments as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
