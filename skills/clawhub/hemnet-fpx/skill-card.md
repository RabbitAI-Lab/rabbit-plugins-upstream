## Description:

Query hemnet.se (Swedish property portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the hemnet-mcp server — resolve locations, search for-sale and sold listings, and read listing detail via one-shot GraphQL calls through a signed-in browser tab. Use when you want Hemnet data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers who want Hemnet property data without running the Hemnet MCP use this skill to resolve Swedish locations, search for-sale and sold listings, and retrieve listing details from the shell.

### Deployment Geography for Use:

Sweden

## Known Risks and Mitigations:

Risk: A paired browser connection may use the session in the open Hemnet tab, and the pairing persists.

Mitigation: Review the CLI and extension, verify the extension download, grant only hemnet.se fetch access, use a logged-out tab to avoid account-session use, and revoke pairing when finished.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell-command examples; GraphQL query results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing amounts are in SEK and areas in square meters.]

## Skill Version(s):

1.1.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
