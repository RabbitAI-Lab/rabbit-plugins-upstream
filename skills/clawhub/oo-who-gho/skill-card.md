## Description:

WHO Global Health Observatory (who.int) skill for requests that search indicators, read indicator observations, and list dimensions or dimension values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to query WHO Global Health Observatory data through the OOMOL oo CLI without handling raw service credentials. It supports indicator search, observation retrieval, and dimension discovery for WHO GHO datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the OOMOL oo CLI.

Mitigation: Review the installer source and prefer an official versioned install path with checksum or signature verification before allowing installation.

Risk: The skill may require signing in to the OOMOL CLI after installation.

Mitigation: Require explicit user approval before running authentication commands, and do not allow an agent to sign in proactively.

## Reference(s):

- [WHO Global Health Observatory homepage](https://www.who.int/data/gho)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-who-gho)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action responses are returned as JSON from the oo CLI when commands are executed.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
