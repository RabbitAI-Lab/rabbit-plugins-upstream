## Description:

IMAP Mailbox lets an agent operate a connected IMAP mailbox through OOMOL, including reading messages, searching folders, downloading attachments, sending messages, and changing mailbox state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to manage an OOMOL-connected IMAP mailbox, including reading/searching mail and performing confirmed send, move, mark, reply, forward, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read and search actions can expose mailbox contents and attachments from the connected IMAP account.

Mitigation: Install and use the skill only for mailboxes the user intends the agent to access, and keep returned message contents within the expected task scope.

Risk: Write and destructive actions can send mail, alter message state, move messages, or delete messages.

Mitigation: Require explicit confirmation of the mailbox, target message or folder, recipient list, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [IMAP RFC 3501](https://www.rfc-editor.org/rfc/rfc3501)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-generic-imap)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request JSON payloads for connector actions and may return mailbox data from the connected account.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
