## Description:

Discover and filter 15,310 The Graph subgraphs by domain, network, protocol type, or natural language goal. Each result includes an x402 query URL — $0.01 USDC on Base per call, no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agents use this skill to discover, compare, and select The Graph subgraphs by domain, network, protocol type, entity, or natural-language goal before issuing GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode exposes local endpoints if enabled.

Mitigation: Use stdio mode by default and enable --http or --http-only only on trusted or firewalled networks.

Risk: x402 query flows can spend wallet funds through a separate x402 client.

Mitigation: Keep wallet signing under explicit user control and review each payment before execution.

Risk: Unpinned installs or dependency updates can change runtime behavior.

Mitigation: Pin subgraph-registry-mcp@0.8.29 and review dependency updates before deployment.

Risk: Bypassing registry database verification can allow untrusted or mismatched data to load.

Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY in agent runtime defaults.

Risk: Semantic search may perform a one-time model download if the bundled model is missing.

Mitigation: Pre-bundle the model or avoid semantic_search_subgraphs in strictly offline environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project Homepage](https://github.com/PaulieB14/subgraph-registry)
- [MCP Server Metadata](artifact/server.json)
- [OpenAPI Specification](artifact/data/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured MCP tool responses with text, JSON-like data, URLs, query examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include subgraph metadata, reliability scores, x402 and legacy query URLs, pricing manifests, schema-change summaries, and generated GraphQL starter queries.]

## Skill Version(s):

0.8.29 (source: server release evidence, package.json, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
