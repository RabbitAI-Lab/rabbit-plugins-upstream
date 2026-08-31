## Description:

Discover and filter 15,333 The Graph subgraphs by domain, network, protocol type, or natural language goal. Each result includes an x402 query URL — $0.01 USDC on Base per call, no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP server to discover reliable The Graph subgraphs, inspect their schemas and query paths, and choose x402 or API-key routes before issuing GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: x402 query URLs can trigger wallet spending when used with an auto-payment client.

Mitigation: Require explicit per-call approval or strict wallet spend limits before enabling x402 auto-payment.

Risk: Running an unpinned npm command can install a newer package than the reviewed release.

Mitigation: Install the pinned package version subgraph-registry-mcp@0.9.10 for reviewed deployments.

Risk: The optional HTTP/SSE transport exposes local endpoints when enabled.

Mitigation: Use the default stdio transport unless HTTP/SSE is intentionally needed in a trusted or firewalled environment.

Risk: Strictly offline runtimes may not allow fallback downloads for missing registry or semantic-search model assets.

Mitigation: Pre-bundle required data and model assets, keep registry hash verification enabled, and avoid semantic search when offline constraints prohibit model downloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Subgraph Registry Repository](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Network](https://thegraph.com)
- [OpenAPI Specification](artifact/data/openapi.json)

## Skill Output:

**Output Type(s):** [text, json, code, configuration, guidance]

**Output Format:** [JSON tool responses with subgraph metadata, reliability scores, query URLs, pricing details, and starter GraphQL queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery-only responses; querying selected subgraphs may require a Graph Studio API key or x402 wallet payment.]

## Skill Version(s):

0.9.10 (source: server-resolved release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
