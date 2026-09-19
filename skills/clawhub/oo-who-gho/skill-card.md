## Description:

WHO Global Health Observatory (who.int) helps agents search indicators and read WHO Global Health Observatory data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search WHO GHO indicators, retrieve indicator observations with filters, and list dimensions or dimension values through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions document remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer source before use and prefer a verified package or direct WHO API access for sensitive research queries.

Risk: Connector use depends on the OOMOL account flow and server-side authentication.

Mitigation: Confirm that OOMOL account handling is acceptable for the intended data workflow before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-who-gho)
- [WHO Global Health Observatory homepage](https://www.who.int/data/gho)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before running WHO Global Health Observatory connector actions; normal listed actions are read-only.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
