## Description:

DataCite helps agents search and retrieve DOI metadata records through OOMOL's DataCite connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect DataCite action schemas, retrieve individual DOI metadata records, and search, filter, sort, and paginate DOI metadata through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI only from a trusted verified source.

Risk: DataCite queries, DOI identifiers, filters, and execution metadata are routed through OOMOL by default.

Mitigation: Use the skill only when routing this information through OOMOL is acceptable for the relevant account and data.

## Reference(s):

- [ClawHub DataCite Skill](https://clawhub.ai/oomol/skills/oo-datacite)
- [DataCite Homepage](https://datacite.org/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch live action schemas before constructing DataCite connector requests and to handle JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
