## Description:

Query hemnet.se (Swedish property portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the hemnet-mcp server — resolve locations, search for-sale and sold listings, and read listing detail via one-shot GraphQL calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can resolve Swedish locations, search active and sold Hemnet listings, and read listing details from scripts using fpx without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser pairing persists and grants the CLI access through the paired browser connection.

Mitigation: Approve only hemnet.se and fetch access, verify the extension download, and revoke pairing when it is no longer needed.

## Reference(s):

- [GraphQL query examples](artifact/references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON GraphQL responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listing data; prices are in SEK and areas are in m².]

## Skill Version(s):

1.1.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
