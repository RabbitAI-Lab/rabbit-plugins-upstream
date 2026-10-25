## Description:

Query booli.se (Swedish property portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the booli-mcp server — resolve areas, search for-sale and sold listings (slutpriser), and read property detail via one-shot GraphQL calls through a signed-in browser tab. Use when you want Booli data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can use the skill to resolve Booli area IDs and search for-sale listings, sold prices, and property details from scripts or shell sessions without running the booli-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paired browser extension uses the browser session and pairing remains active until revoked.

Mitigation: Verify the extension release checksum, approve only booli.se fetch access, and revoke pairing when it is no longer needed.

## Reference(s):

- [GraphQL query examples](artifact/references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ContextMint Bridge source repository](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases and checksums](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions with shell commands and JSON GraphQL query bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booli query results are JSON and can be filtered with jq.]

## Skill Version(s):

2.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
