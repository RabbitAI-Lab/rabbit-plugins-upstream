## Description:

Use this skill for PlanetScale requests - reading, creating, updating, and deleting data - instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect PlanetScale connector schemas and run read, write, and destructive PlanetScale organization, database, and branch actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-line remote installer commands execute downloaded code immediately.

Mitigation: Use a verified oo CLI package when available, or inspect and verify the installer before running it.

Risk: Write and destructive connector actions can create or delete PlanetScale databases and branches.

Mitigation: Inspect the live action schema, confirm the exact payload and target with the user, and require explicit approval before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-planetscale)
- [PlanetScale homepage](https://planetscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read or modify PlanetScale resources after inspecting live action schemas.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
