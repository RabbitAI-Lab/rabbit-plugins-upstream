## Description:

Operates a connected NetEase Mail account through the OOMOL oo CLI for reading, searching, sending, replying, forwarding, moving, marking, deleting, and downloading email content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected NetEase Mail mailbox from an agent, including reading mail, finding messages, sending responses, and managing message state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the oo CLI installation path first; prefer a verified package, pinned release, checksum, or inspected installer.

Risk: Connected actions can access mailbox content and change or delete messages.

Mitigation: Confirm write and destructive action payloads with the user before execution.

## Reference(s):

- [ClawHub NetEase Mail skill page](https://clawhub.ai/oomol/skills/oo-netease-mail)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [NetEase Mail homepage](https://mail.163.com/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data and can read, send, move, mark, or delete mailbox messages.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
