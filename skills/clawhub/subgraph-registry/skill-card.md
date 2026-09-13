## Description:

Same abilities as graphops/subgraph-mcp with better discovery: search 15,337+ classified subgraphs, see real 30-day query volume on every hit, and use opt-in schema and execute tools under official-compatible names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to discover, compare, and select subgraphs on The Graph Network before optionally running GraphQL schema or query calls. It is especially suited for agents that need subgraph IDs, reliability signals, query volume, starter queries, or official-compatible MCP tool names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional HTTP/SSE transport can expose API-key-backed query tools to reachable clients.

Mitigation: Use the default stdio or loopback transport for normal use; if HTTP/SSE is enabled, place it behind authentication and network controls.

Risk: Unpinned run commands can install a newer, unreviewed release.

Mitigation: Install a pinned, reviewed version such as subgraph-registry-mcp@0.10.2.

Risk: Opt-in gateway query tools can spend Graph Studio API quota when credentials are configured.

Mitigation: Only configure Graph Studio API keys in trusted runtimes and monitor quota usage.

Risk: x402 URLs represent paid query routes that require a wallet-enabled client.

Mitigation: Treat x402 URLs as caller-managed payment routes; this server does not auto-pay them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Publisher profile](https://clawhub.ai/user/paulieb14)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Network](https://thegraph.com)
- [Official subgraph MCP](https://github.com/graphops/subgraph-mcp)
- [OpenAPI specification](openapi.yaml)
- [MCP server manifest](server.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, JSON examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return subgraph metadata, query URLs, starter GraphQL, credential-required notices, and optional local HTTP/SSE setup guidance.]

## Skill Version(s):

0.10.2 (source: package.json, server.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
