## Description:

Discover and filter 15,330 The Graph subgraphs by domain, network, protocol type, or natural language goal; each result includes an x402 query URL for $0.01 USDC on Base per call with no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agents use this MCP server to discover relevant The Graph subgraphs, compare reliability signals, retrieve query URLs, and get schema-aware guidance before querying blockchain data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installs can pull a newer package version than the one reviewed.

Mitigation: Pin the npm package version before using the server in an autonomous-agent runtime.

Risk: Disabling registry hash verification can allow tampered or unexpected registry data to load.

Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY in normal runtime configuration.

Risk: HTTP/SSE mode exposes a local server surface when enabled.

Mitigation: Use the default stdio transport unless HTTP/SSE is needed, and run HTTP/SSE only in trusted or firewalled environments.

Risk: Returned x402 URLs can lead wallet-enabled agents to spend funds on paid GraphQL queries.

Mitigation: Apply wallet spending limits and require policy checks before an agent signs x402 payments.

Risk: Semantic search may download its embedding model from Hugging Face if the model is not bundled.

Mitigation: Pre-bundle the model or avoid semantic_search_subgraphs in strictly offline runtimes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Publisher Profile](https://clawhub.ai/user/paulieb14)
- [Project Homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [The Graph Studio API Keys](https://thegraph.com/studio/apikeys/)
- [Graph Protocol x402 Client](https://www.npmjs.com/package/@graphprotocol/client-x402)
- [Glama MCP Listing](https://glama.ai/mcp/servers/PaulieB14/subgraph-registry)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [JSON MCP tool responses with subgraph metadata, query URLs, pricing details, and query guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paid x402 query URLs, legacy API-key query URLs, reliability scores, schema details, and registry statistics.]

## Skill Version(s):

0.9.4 (source: package.json, server.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
