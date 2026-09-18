## Description:

InfoLobby (infolobby.com). Use this skill for ANY InfoLobby request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect InfoLobby action schemas and run read, create, update, delete, count, and query operations against InfoLobby workspaces and tables through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts for the oo CLI.

Mitigation: Review setup commands before installation, prefer independently verified OOMOL documentation or a package manager with publisher verification, and require explicit approval before running an installer.

Risk: Create, update, and delete actions can change or remove InfoLobby data.

Mitigation: Inspect the live action schema, show the exact payload and expected effect, and get explicit user confirmation before write or destructive actions.

## Reference(s):

- [InfoLobby homepage](https://infolobby.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-infolobby)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector schema and run commands; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
