## Description:

HigherGov helps agents search and read HigherGov data, including agencies, contracts, NAICS codes, and opportunities through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query HigherGov through an OOMOL-connected account for public-sector agency, contract, NAICS, and opportunity data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Prefer verified, versioned, checksum- or signature-validated oo CLI installation sources before using the skill.

Risk: The skill sends HigherGov connector requests through an OOMOL-connected account.

Mitigation: Install only when OOMOL and HigherGov connector traffic are acceptable, and connect only accounts intended for agent queries.

## Reference(s):

- [HigherGov homepage](https://www.highergov.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector data with execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
