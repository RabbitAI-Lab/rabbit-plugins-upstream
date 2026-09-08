## Description:

NetEase Enterprise Mail (qiye.163.com). Use this skill for NetEase Enterprise Mail requests that read, create, update, or delete mailbox data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a connected NetEase Enterprise Mail account, including reading folders and messages, searching mail, sending or replying to email, moving or marking messages, deleting messages, and downloading attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send email, reply or forward messages, move or mark messages, download attachments, and delete messages in the connected mailbox.

Mitigation: Confirm the exact target, payload, and expected effect before running send, move, mark, or delete actions; require explicit approval for destructive deletion.

Risk: The setup instructions include remote oo CLI installer commands.

Mitigation: Verify the oo CLI installation source before running installer commands, and use first-time setup only after an auth, connection, or missing-command failure.

Risk: Connector action contracts can change over time.

Mitigation: Inspect the live connector schema before building each action payload so requests match the current contract.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-netease-enterprise-mail)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [NetEase Enterprise Mail Homepage](https://qiye.163.com/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to inspect live connector schemas before running oo CLI actions against the connected NetEase Enterprise Mail account.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
