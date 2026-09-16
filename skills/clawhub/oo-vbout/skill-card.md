## Description:

VBOUT (vbout.com) skill for reading, creating, updating, and deleting VBOUT data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate VBOUT account, list, and contact workflows through OOMOL-connected connector actions. It supports reading account/list/contact data and performing confirmed create, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include commands that execute downloaded installer scripts without verification.

Mitigation: Use official, verifiable installation steps or inspect and verify the installer before running first-time setup commands.

Risk: The skill can create, update, or delete VBOUT marketing contacts and list data.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval before destructive delete actions.

Risk: VBOUT operations rely on OOMOL as the intermediary for connector execution and credential handling.

Mitigation: Install only when the user is comfortable using OOMOL for VBOUT operations.

## Reference(s):

- [VBOUT homepage](https://www.vbout.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vbout)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected VBOUT account; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
