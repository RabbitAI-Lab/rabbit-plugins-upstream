## Description:

Helps agents query public Booli property listings, sold prices, and property details from a shell without running the Booli MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up Swedish property areas, for-sale and sold listings, and property details through an existing browser tab when they need Booli data in a script or without an MCP server.

### Deployment Geography for Use:

Global (property data covers Sweden)

## Known Risks and Mitigations:

Risk: The required browser extension can access sites permitted by its site-access setting.

Mitigation: Install the fpx CLI and ContextMint Bridge only if comfortable with them, and limit extension site access to booli.se.

Risk: Automated property queries may exceed intended use of Booli's public data.

Mitigation: Query public property data only and comply with Booli's terms.

## Reference(s):

- [Booli FPX skill release](https://clawhub.ai/chrischall/skills/booli-fpx)
- [Booli GraphQL query examples](artifact/references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and GraphQL JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are in SEK; floor area is in m².]

## Skill Version(s):

2.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
