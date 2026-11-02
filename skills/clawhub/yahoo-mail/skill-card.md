## Description:

Connect to Yahoo Mail over IMAP and SMTP with an app-specific password to read, search, send, reply to, forward, and organize email, drafts, threads, and folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

People who want an agent to work with a Yahoo Mail mailbox can use this skill to read and search messages, manage drafts, threads, and folders, and send or organize email. It also documents user-approved hosted and local automations for Yahoo Mail tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the skill gives it access to the selected mailbox, including the ability to send or delete email.

Mitigation: Use a separate app password, select the intended connection, and review and approve every write, send, or new connection.

Risk: Hosted functions and triggers can perform mailbox actions on schedules or events and may deliver events to configured destinations.

Mitigation: Use a dedicated Maton account with only necessary connections; review the code, destinations, and schedules, and remove the automation when finished.

Risk: External packages and hosted automation security guarantees have not been independently audited.

Mitigation: Review the code and automation configuration before use, and keep hosted automations limited to the connections and destinations needed for the task.

## Reference(s):

- [Yahoo Mail on ClawHub](https://clawhub.ai/maton/skills/yahoo-mail)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Yahoo: generate and manage app passwords](https://help.yahoo.com/kb/SLN15241.html)
- [Yahoo: IMAP server settings](https://help.yahoo.com/kb/SLN4075.html)
- [RFC 3501: IMAP4rev1](https://www.rfc-editor.org/rfc/rfc3501)
- [RFC 8474: IMAP extension for object identifiers](https://www.rfc-editor.org/rfc/rfc8474)
- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions, Email data]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Email content may include private information; consequential mailbox actions require user approval.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
