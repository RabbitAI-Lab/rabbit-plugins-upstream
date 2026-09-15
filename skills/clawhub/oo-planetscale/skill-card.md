## Description:

Operate PlanetScale through an OOMOL-connected account using the oo CLI for database, branch, and organization read and management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect PlanetScale connector schemas and run OOMOL CLI commands for organizations, databases, and branches, including guarded write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running remote installer scripts directly in a shell.

Mitigation: Install the OOMOL CLI from a verified, versioned source with integrity checks, and do not allow an agent to run the remote installer automatically.

Risk: Write and destructive PlanetScale actions can change or delete databases and branches.

Mitigation: Confirm the exact organization, database, branch, action, and JSON payload with the user before approving any write or destructive command.

## Reference(s):

- [PlanetScale Homepage](https://planetscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
