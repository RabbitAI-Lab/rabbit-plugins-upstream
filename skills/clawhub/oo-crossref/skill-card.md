## Description:

Use this Crossref skill for searching and reading Crossref data, retrieving DOI metadata, exporting citations, and matching bibliographic references through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Crossref works and resources, retrieve DOI metadata and agencies, export citations, and match bibliographic references without calling the Crossref API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance documents remote installer commands that execute downloaded shell or PowerShell scripts directly.

Mitigation: Install the oo CLI only through a verified, versioned, checksum-checked method before using the skill.

Risk: Crossref queries are routed through OOMOL as an intermediary.

Mitigation: Use the skill only when that intermediary access pattern is acceptable for the data being queried.

## Reference(s):

- [ClawHub Crossref Skill](https://clawhub.ai/oomol/skills/oo-crossref)
- [Crossref](https://www.crossref.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL connector responses that may include JSON data and an execution identifier.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
