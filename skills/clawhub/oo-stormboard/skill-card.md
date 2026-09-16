## Description:

Stormboard connector for searching and reading Stormboard data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Stormboard profiles, storms, access levels, participants, tags, ideas, connectors, templates, and template categories from an OOMOL-connected Stormboard account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote installer execution.

Mitigation: Review OOMOL's official installation process and prefer a verified package or installer with a checksum or signature before installing.

Risk: Stormboard requests are sent through OOMOL and require an OOMOL-connected Stormboard account.

Mitigation: Use an account and workspace appropriate for the data being accessed, and confirm OOMOL and Stormboard access requirements before routine use.

## Reference(s):

- [Stormboard homepage](https://stormboard.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Stormboard skill page](https://clawhub.ai/oomol/skills/oo-stormboard)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before issuing requests; routine actions described in evidence are read-only.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
