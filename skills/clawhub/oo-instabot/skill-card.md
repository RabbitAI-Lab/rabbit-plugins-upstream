## Description:

Instabot operations for reading, creating, updating, deleting, and restoring user data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Instabot users through an OOMOL-connected account. It supports read, create, update, soft-delete, restore, and changed-since synchronization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions execute remote installer scripts directly in a shell.

Mitigation: Review the OOMOL CLI installation path first, prefer official version-pinned instructions with checksum or signature verification, and avoid piping remote scripts directly into Bash or PowerShell.

Risk: Create, update, delete, and restore actions can change Instabot account state.

Mitigation: Inspect the live connector schema before preparing payloads and get explicit user confirmation for the exact payload and effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instabot)
- [Instabot homepage](https://www.instabot.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
