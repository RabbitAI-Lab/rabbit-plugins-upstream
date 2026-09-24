## Description:

Provides a command-line Python tool for sending, reading, searching, organizing, and downloading attachments from 163.com mailboxes over IMAP and SMTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[newolf20000](https://clawhub.ai/user/newolf20000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and mailbox operators use this skill to let an agent manage 163.com email workflows, including sending messages, reading and searching mailbox contents, organizing folders, marking messages, and downloading attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles mailbox credentials and can read, send, and manage email content.

Mitigation: Install only when this mailbox access is acceptable, use a 163.com client authorization code, and protect or rotate the code if exposure is suspected.

Risk: Bulk delete, move, mark, and expunge actions can alter or remove mailbox data.

Mitigation: Review the target folder and message IDs before destructive commands, especially when using all-message or expunge options.

Risk: Attachment downloads may expose the user to unsafe attachment content and the evidence flags filename-containment concerns.

Mitigation: Download attachments only to a contained directory, inspect filenames and content before opening them, and avoid untrusted attachments until filename containment is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/newolf20000/skills/email-163-com)
- [README.md](artifact/README.md)
- [SECURITY.md](artifact/SECURITY.md)
- [INSTALL.md](artifact/INSTALL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration]

**Output Format:** [Command-line text output with JSON configuration snippets and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured 163.com mailbox address and client authorization code; operations can read, send, move, mark, delete, and download mailbox content.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
