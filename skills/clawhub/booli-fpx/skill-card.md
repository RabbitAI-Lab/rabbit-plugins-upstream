## Description:

Helps agents query Swedish property listings, sold prices, and property details on Booli through browser-routed GraphQL calls using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Swedish property areas, search active and sold listings, and retrieve property details without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-extension routing can expose active browser sessions to the paired extension.

Mitigation: Verify the extension release or source, use a dedicated Chrome profile or tab with minimal sensitive sessions, and limit site access to booli.se.

Risk: A small sample of sold listings can produce misleading market statistics.

Mitigation: Check the result count before relying on a derived median or average.

## Reference(s):

- [Booli GraphQL query examples](references/graphql-queries.md)
- [Booli Fpx on ClawHub](https://clawhub.ai/chrischall/skills/booli-fpx)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property prices in SEK and areas in square metres; live results depend on Booli and an available paired browser tab.]

## Skill Version(s):

2.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
