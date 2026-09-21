## Description:

Subgraph Registry MCP helps agents discover 15,385+ classified subgraphs with 30-day query volume, reliability signals, opt-in schema inspection, and opt-in GraphQL execution under official tool names while keeping discovery tools query-free.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to discover, inspect, and optionally query classified subgraphs on The Graph Network. It helps agents choose relevant subgraphs by domain, network, reliability, query volume, schema details, and contract coverage before executing GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode can expose API-key-backed query tools without built-in authentication if deployed remotely.

Mitigation: Keep the server on stdio or loopback for normal use; if HTTP/SSE is exposed, place it behind authentication, network controls, and rate limits.

Risk: API keys for The Graph gateway can be exposed or misused in shared or remote environments.

Mitigation: Set `THE_GRAPH_STUDIO_API_KEY`, `GRAPH_STUDIO_API_KEY`, or `GATEWAY_API_KEY` only in trusted runtimes and avoid exposing keyed transports publicly.

Risk: Unpinned installation can pull a newer npm package or dependency set than the reviewed release.

Mitigation: Pin `subgraph-registry-mcp@0.10.4` and production dependencies before deployment.

Risk: `semantic_search_subgraphs` may download a missing embedding model from Hugging Face, which is not suitable for strictly offline runtimes.

Mitigation: Use the bundled model where available or skip semantic search in offline deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project Homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [Official subgraph MCP](https://github.com/graphops/subgraph-mcp)
- [Graph Studio API Keys](https://thegraph.com/studio/apikeys/)
- [Glama MCP Server Listing](https://glama.ai/mcp/servers/PaulieB14/subgraph-registry)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and structured MCP tool responses, including JSON, GraphQL examples, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery tools use a local bundled registry; optional schema and query tools may call The Graph gateway only when explicitly invoked with credentials.]

## Skill Version(s):

0.10.4 (source: evidence.json release.version, package.json, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
