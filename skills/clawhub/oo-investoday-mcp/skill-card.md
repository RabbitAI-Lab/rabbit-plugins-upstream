## Description:

Investoday MCP (data-api.investoday.net) helps agents search and read Investoday financial market data through the OOMOL `oo` connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Investoday MCP for realtime stock quotes, stock reference data, valuation indicators, adjusted historical prices, market breadth, announcements, and research reports through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run a remote installer script in the shell.

Mitigation: Review the installer source before use, prefer a trusted pinned package or verified release, and connect the Investoday account or API key only after confirming the connector and billing implications.

Risk: Live connector schemas and billing or connection state can change outside the skill artifact.

Mitigation: Inspect the current action schema before each payload and retry setup only after authentication, scope, credential, app, or billing errors.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-investoday-mcp)
- [Investoday MCP Homepage](https://data-api.investoday.net/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Investoday MCP action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
