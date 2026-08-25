## Description:

MarketTime (markettime.com). Use this skill for ANY MarketTime request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read MarketTime catalog, manufacturer, and order data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access MarketTime order, catalog, and manufacturer data available to the user's connected OOMOL account.

Mitigation: Install only for agents that should read MarketTime data, and review future versions carefully if they add write or destructive actions.

Risk: Connector calls may fail when the CLI is not installed, the user is not signed in, the MarketTime connection is missing or expired, or billing credit is insufficient.

Mitigation: Use the documented setup and recovery steps only after a matching command failure.

## Reference(s):

- [MarketTime homepage](https://www.markettime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns structured connector responses with execution IDs.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
