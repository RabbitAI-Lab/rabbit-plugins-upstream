## Description:

Operates OOMOL Console through the OOMOL Console connector for reading, creating, updating, and deleting team, billing, usage, member, Connection, and permission-group data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External OOMOL Console administrators and operators use this skill to inspect account, team, member, billing, usage, Connection, and permission-group state and to perform confirmed Console changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes an unverified remote installer for the oo CLI.

Mitigation: Install the oo CLI manually from a verified, pinned, or checksum-validated source before using the skill.

Risk: The skill can perform write and destructive OOMOL Console actions for members and permission groups.

Mitigation: Confirm the exact target, payload, and effect with the user before write actions, and require explicit approval for destructive actions.

Risk: Action payloads may become incorrect if connector contracts change.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [OOMOL Console homepage](https://console.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
