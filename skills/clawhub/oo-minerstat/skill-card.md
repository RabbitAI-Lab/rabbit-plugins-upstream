## Description:

Minerstat (minerstat.com). Use this skill for ANY Minerstat request: searching and reading data through the OOMOL-connected Minerstat connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Minerstat coin profitability, market, mining hardware, and pool data through the oo CLI without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could be run directly in a shell if the oo CLI is missing.

Mitigation: Install the oo CLI only from a verified trusted source, review installer contents before execution, and avoid elevated privileges unless required.

Risk: Connector commands depend on an authenticated OOMOL account and a connected Minerstat API key.

Mitigation: Run setup, login, or connection recovery steps only after a connector command fails with the matching authentication or connection error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-minerstat)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Minerstat homepage](https://minerstat.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
