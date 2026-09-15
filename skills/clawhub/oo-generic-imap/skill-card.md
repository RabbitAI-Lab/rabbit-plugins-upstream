## Description:

Operate a connected IMAP mailbox through OOMOL's oo CLI and generic_imap connector to read, search, send, reply to, forward, move, mark, delete, and download mailbox content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected IMAP mailbox from an agent, including reading folders and messages, searching mail, downloading attachments, sending mail, and managing message state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that execute directly in the shell.

Mitigation: Prefer an inspected, signed, and version-pinned oo CLI installation path instead of running pipe-to-shell installers as written.

Risk: Mailbox write actions can send email or change message state, and delete_email removes messages.

Mitigation: Require explicit user approval for send, reply, forward, move, mark, and delete actions, with the exact target and payload confirmed before execution.

## Reference(s):

- [IMAP4rev1 RFC 3501](https://www.rfc-editor.org/rfc/rfc3501)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-generic-imap)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect connector schemas or run mailbox actions and may summarize JSON action responses.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
