## Description:

NetEase Mail (mail.163.com). Use this skill for ANY NetEase Mail request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected NetEase Mail account for mailbox reading, search, attachment download, message composition, replies, forwarding, marking, moving, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send, forward, reply to, mark, move, or delete NetEase Mail messages through a connected account.

Mitigation: Require clear user confirmation of the exact payload and expected effect before write or destructive mail actions.

Risk: The first-time setup path includes a one-line CLI installer.

Mitigation: Review the oo CLI installation method before running the installer and only use setup steps when commands fail for the matching reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netease-mail)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [NetEase Mail homepage](https://mail.163.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before running NetEase Mail actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
