## Description:

Query Polymarket prediction market data via The Graph subgraphs and Polymarket REST APIs for market search, live prices, on-chain analytics, trader P&L, open interest, resolution status, and CLOB V2 builder attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this MCP server to let assistants query Polymarket market data, live CLOB prices, order books, subgraph analytics, trader positions, open interest, and resolution status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated HTTP/SSE mode can expose the MCP server if used on an untrusted network.

Mitigation: Prefer stdio/local use; when enabling --http or --http-only, bind to localhost or place the service behind authentication, TLS, and firewall controls.

Risk: Connected clients can consume the GRAPH_API_KEY query quota.

Mitigation: Treat GRAPH_API_KEY as a secret and only connect trusted clients that are allowed to use the associated quota.

Risk: Dependency posture requires review before remote use.

Mitigation: Review dependencies and scan the package before remote deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/graph-polymarket-mcp)
- [npm package](https://www.npmjs.com/package/graph-polymarket-mcp)
- [MCP Registry entry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.PaulieB14/graph-polymarket-mcp)
- [The Graph Studio](https://thegraph.com/studio/)
- [Polymarket](https://polymarket.com/)
- [Smithery server page](https://smithery.ai/servers/paulieb14/graph-polymarket-mcp)
- [Glama server page](https://glama.ai/mcp/servers/@PaulieB14/graph-polymarket-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted text returned through MCP tool responses, plus setup commands and client configuration examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js; The Graph subgraph tools require GRAPH_API_KEY, while Polymarket REST tools can run without an API key.]

## Skill Version(s):

2.1.1 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
