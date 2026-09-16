## Description:

Breezy HR (breezy.hr) lets agents search and read Breezy HR data through OOMOL-connected oo CLI actions instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, recruiters, and developers use this skill to inspect Breezy HR companies, positions, candidates, and the current authenticated user through an OOMOL-connected account. It supports read-oriented recruiting workflows, including listing position candidates and searching candidates by exact normalized email address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer pipelines that can execute code on the user's machine.

Mitigation: Use a verified, pinned, or package-manager-based oo CLI installation path, and run installer pipelines only after the organization has approved the OOMOL installer source.

Risk: Breezy HR candidate and recruiting data may be accessed through OOMOL-connected infrastructure.

Mitigation: Confirm that the organization's HR, privacy, and vendor-use policies allow Breezy HR data to be handled through OOMOL before using the connector.

## Reference(s):

- [ClawHub Breezy HR Skill Page](https://clawhub.ai/oomol/skills/oo-breezy-hr)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Breezy HR Homepage](https://breezy.hr/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
