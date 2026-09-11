## Description:

Protocol-wide on-chain analytics for Limitless prediction markets on Base: trader P&L, top traders, market and daily volume history, liquidity events, and raw GraphQL from the Limitless subgraphs on The Graph's decentralized network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to query read-only on-chain analytics for Limitless prediction markets on Base, including market activity, trader profiles, positions, P&L, liquidity events, and raw subgraph GraphQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The npm install path may run unreviewed or changed package code.

Mitigation: Review the npm package before enabling the skill and pin the command to a specific reviewed version such as 1.1.0.

Risk: Credential handling may expose unrelated environment variables to the MCP process.

Mitigation: Provide only the intended GRAPH_API_KEY and avoid exposing unrelated credentials such as LIMITLESS_API_KEY unless that behavior is required and reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/graph-limitless-mcp)
- [Graph Limitless MCP npm Package](https://www.npmjs.com/package/graph-limitless-mcp)
- [The Graph API Keys](https://thegraph.market/dashboard#api-keys)
- [Limitless](https://limitless.exchange)
- [The Graph](https://thegraph.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown or text responses with MCP tool calls and optional shell install command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and GRAPH_API_KEY; tool behavior is described as read-only analytics.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
