## Description:

NetEase Enterprise Mail helps an agent read, search, send, reply to, forward, move, mark, and delete messages through an OOMOL-connected NetEase Enterprise Mail account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to manage NetEase Enterprise Mail messages from an agent workflow, including mailbox inspection, message retrieval, sending, replies, forwarding, movement, read-state updates, attachment downloads, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can lead an agent to run remote installer scripts before handling sensitive mail access.

Mitigation: Review the OOMOL CLI installation path first and prefer a verified, version-pinned installer or package manager flow.

Risk: The skill can change mailbox state by sending, replying, forwarding, moving, marking, or deleting email.

Mitigation: Use only the intended NetEase Enterprise Mail account and require explicit user confirmation before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netease-enterprise-mail)
- [NetEase Enterprise Mail homepage](https://qiye.163.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
