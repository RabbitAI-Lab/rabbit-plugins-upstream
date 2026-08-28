## Description:

Discover and filter 15,330 The Graph subgraphs by domain, network, protocol type, or natural language goal. Each result includes an x402 query URL - $0.01 USDC on Base per call, no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP server to discover reliable The Graph subgraphs, inspect schema and endpoint details, and choose x402 or legacy query paths before running GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned x402 URLs can lead to paid GraphQL queries when used with a funded signing wallet.

Mitigation: Require explicit user approval and wallet policy checks before an agent follows x402 URLs or signs USDC payments.

Risk: Optional HTTP/SSE mode exposes a local server interface when enabled.

Mitigation: Use the default stdio transport for local clients, and only enable --http or --http-only in trusted or firewalled environments.

Risk: Unpinned npm execution can install a newer package than the reviewed release.

Mitigation: Install and run the pinned package version subgraph-registry-mcp@0.8.31.

Risk: Semantic search may require a one-time model download if the bundled ONNX model is unavailable.

Mitigation: Pre-bundle the model or avoid semantic_search_subgraphs in strictly offline runtimes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Publisher profile](https://clawhub.ai/user/paulieb14)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [@graphprotocol/client-x402](https://www.npmjs.com/package/@graphprotocol/client-x402)
- [Glama MCP server listing](https://glama.ai/mcp/servers/PaulieB14/subgraph-registry)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSON MCP tool responses with subgraph metadata, query URLs, pricing manifests, and example GraphQL queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery results may include paid x402 query endpoints, legacy API-key endpoints, local HTTP/SSE configuration, and optional semantic-search behavior.]

## Skill Version(s):

0.8.31 (source: package.json, server evidence, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
