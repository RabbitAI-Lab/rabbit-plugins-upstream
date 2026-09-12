## Description:

Query hemnet.se (Swedish property portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the hemnet-mcp server, resolving locations, searching for-sale and sold listings, and reading listing detail via one-shot GraphQL calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Hemnet property data from shell workflows without running the Hemnet MCP server. It supports location autocomplete, active listing search, sold listing search, and listing detail retrieval through prepared GraphQL calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on @fetchproxy/cli and the Transporter extension creating a persistent Hemnet-scoped browser bridge.

Mitigation: Limit browser site access to hemnet.se, consider a separate or logged-out browser profile, and confirm pairing state before use.

Risk: A third-party browser-proxy CLI can change behavior across releases.

Mitigation: Prefer a pinned, reviewed @fetchproxy/cli version and review generated fpx commands before execution.

Risk: GraphQL responses may include errors even when the transport command exits successfully.

Mitigation: Check the response for a GraphQL errors array before relying on listing or market data.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be executed by an agent or user with fpx, jq, the Transporter browser extension, and a Hemnet browser tab configured.]

## Skill Version(s):

0.6.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
