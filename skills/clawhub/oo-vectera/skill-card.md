## Description:

Vectera lets agents read, create, and update Vectera data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Vectera meeting rooms, permissions, settings, and connected-user information through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Use a trusted package source or verify the installer through an official, integrity-checked process before running installation commands.

Risk: Write actions can create or update Vectera meeting rooms, permissions, and settings.

Mitigation: Confirm the exact payload and expected effect with the user before executing any write action.

## Reference(s):

- [ClawHub Vectera Skill](https://clawhub.ai/oomol/skills/oo-vectera)
- [Vectera Homepage](https://go.vectera.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write actions require payload and effect confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
