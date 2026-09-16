## Description:

Use this skill for Finage (finage.co.uk) requests - reading, creating, and updating data through the OOMOL Finage connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Finage market data through an OOMOL-connected account, including stock aggregates, quotes, trades, previous closes, snapshots, and symbol lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installation path before use, prefer a verified versioned release or package manager, and do not allow an agent to run remote installer commands automatically.

Risk: Use depends on an installed, signed-in, and Finage-connected oo CLI.

Mitigation: Run authentication or connection setup only after a command fails with a matching auth or connection error, and keep Finage credentials managed through the OOMOL connection.

## Reference(s):

- [Finage homepage](https://finage.co.uk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are returned as JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
