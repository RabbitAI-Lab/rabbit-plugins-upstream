## Description:

Pilvio (pilvio.com). Use this skill for searching and reading Pilvio account data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Pilvio user, billing, location, and virtual machine data from an OOMOL-connected account. It guides the agent to inspect each live connector schema before running read actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-hosted installer commands that execute directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified or package-manager installation of the `oo` CLI.

Risk: The skill operates through OOMOL-mediated access to Pilvio account data.

Mitigation: Install and use it only when OOMOL-mediated read access to the relevant Pilvio account is acceptable.

## Reference(s):

- [ClawHub Pilvio Skill](https://clawhub.ai/oomol/skills/oo-pilvio)
- [Pilvio Homepage](https://pilvio.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces connector schema and run command guidance; read actions return JSON data from Pilvio through OOMOL.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
