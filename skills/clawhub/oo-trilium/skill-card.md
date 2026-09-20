## Description:

TriliumNext Notes (triliumnotes.org). Use this skill for ANY TriliumNext Notes request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read, create, update, search, and delete TriliumNext Notes content through the OOMOL Trilium connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, overwrite, or delete TriliumNext Notes data.

Mitigation: Require clear user confirmation of the exact payload, target, and expected effect before running write or destructive actions.

Risk: First-time setup may run a remote oo CLI installer.

Mitigation: Review the installer source and use the official install guide before running installation commands.

Risk: The connector uses OOMOL as an intermediary for TriliumNext Notes operations.

Mitigation: Install and use the skill only when the user accepts OOMOL's role in handling the connected workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trilium)
- [TriliumNext Notes homepage](https://triliumnotes.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Trilium icon](https://static.oomol.com/logo/third-party/trilium.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and can return JSON connector responses.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
