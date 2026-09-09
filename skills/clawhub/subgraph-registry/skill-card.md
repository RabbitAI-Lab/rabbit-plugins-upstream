## Description:

Same abilities as graphops/subgraph-mcp with better discovery: search classified subgraphs, see real 30-day query volume on every hit, and opt in to schema or execute tools under the official tool names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this MCP server to discover reliable The Graph subgraphs before querying them. It helps select subgraphs by network, protocol type, schema details, contract address, query volume, and reliability, with opt-in GraphQL execution when the caller supplies a Graph Studio key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode can expose unauthenticated endpoints that may use the operator's Graph API key.

Mitigation: Use default stdio or loopback-only HTTP for local use; do not expose --http or --http-only on shared networks with THE_GRAPH_STUDIO_API_KEY, GRAPH_STUDIO_API_KEY, or GATEWAY_API_KEY set unless an authenticating proxy is in front.

Risk: semantic_search_subgraphs may need network access if the bundled ONNX model is missing.

Mitigation: Bundle or pre-cache the model for offline deployments, or avoid semantic_search_subgraphs in strictly offline runtimes.

Risk: Bypassing registry.db hash verification can allow a modified local registry to load.

Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY=1 in agent-runtime defaults; keep the package-pinned registry hash check enabled.

Risk: External x402 queries can spend USDC if a caller posts to the returned x402 URL with a funded signing client.

Mitigation: Require an explicit payment policy before using x402 clients, and prefer the keyed gateway route when the operator already has Graph Studio credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [MCP server manifest](artifact/server.json)
- [OpenAPI specification](artifact/openapi.yaml)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Configuration, Guidance]

**Output Format:** [MCP tool responses with JSON payloads, schema text, GraphQL examples, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery tools use the local registry; execute and live schema tools require caller-provided Graph gateway credentials.]

## Skill Version(s):

0.10.1 (source: evidence.release.version, artifact/package.json, artifact/server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
