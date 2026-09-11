## Description:

Same abilities as graphops/subgraph-mcp with better discovery. Search 15,337+ classified subgraphs; real 30-day query volume on every hit; opt-in schema and execute under the official tool names. Discovery tools never auto-query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP server to discover, rank, inspect, and optionally query classified subgraphs on The Graph Network. Discovery tools run against a local registry, while schema introspection and GraphQL execution are opt-in actions that require caller intent and, for keyed gateway access, a configured Graph Studio API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode can expose MCP endpoints while a Graph Studio API key is configured.

Mitigation: Prefer stdio or loopback-only HTTP, and place authentication or a trusted proxy in front of /sse and /messages before exposing them to any network.

Risk: Unpinned install examples can pull a newer package than the one reviewed.

Mitigation: Install the reviewed package version explicitly, for example subgraph-registry-mcp@0.10.2, and pin dependencies for reproducible deployments.

Risk: Opt-in execute and live schema tools can send requests to The Graph gateway when credentials are present.

Mitigation: Keep discovery workflows separate from execution, configure THE_GRAPH_STUDIO_API_KEY or GATEWAY_API_KEY only in trusted runtimes, and review tool calls before allowing live gateway access.

## Reference(s):

- [Subgraph Registry repository](https://github.com/PaulieB14/subgraph-registry)
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [The Graph Network](https://thegraph.com)
- [Graph Studio API keys](https://thegraph.com/studio/apikeys/)
- [graphops subgraph MCP](https://github.com/graphops/subgraph-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-like tool results, GraphQL examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery outputs can include ranked subgraph matches, query volume, reliability scores, example GraphQL queries, schema metadata, query URLs, and credential-required guidance for opt-in execution.]

## Skill Version(s):

0.10.2 (source: package.json, server evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
