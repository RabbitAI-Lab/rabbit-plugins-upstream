## Description:

Helps agents query public Hemnet property listings from a shell using the fpx CLI and a user-approved browser bridge instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish locations, search for-sale and sold Hemnet properties, and retrieve listing details through anonymous browser-mediated queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI and browser extension adds third-party software and browser access.

Mitigation: Verify the package and extension release sources, and restrict extension site access to hemnet.se.

Risk: Queries could exceed the disclosed anonymous property-data use.

Mitigation: Use only anonymous public Hemnet property queries and follow hemnet.se's terms.

## Reference(s):

- [Hemnet fpx skill release](https://clawhub.ai/chrischall/skills/hemnet-fpx)
- [GraphQL query examples](artifact/references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return public listing data, with prices in SEK and areas in m².]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
