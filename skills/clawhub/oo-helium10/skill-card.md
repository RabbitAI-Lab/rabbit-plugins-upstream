## Description:

Helium 10 helps an agent search and read Helium 10 data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sellers, operators, and developers use this skill to discover available Helium 10 tools and run approved read-only Helium 10 actions through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Require deliberate user approval before running installer commands and prefer a reviewable installation method when possible.

Risk: The connector surface may change to expose non-read actions in the future.

Mitigation: Fetch the live action schema before use and require explicit user confirmation for any write or destructive action.

## Reference(s):

- [ClawHub Helium 10 Skill](https://clawhub.ai/oomol/skills/oo-helium10)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Helium 10 Homepage](https://www.helium10.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when commands are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
