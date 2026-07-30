## Description: <br>
Discover and filter 15,251 The Graph subgraphs by domain, network, protocol type, or natural language goal; each result includes an x402 query URL at $0.01 USDC on Base per call, with no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to discover suitable The Graph subgraphs, compare reliability signals, retrieve query endpoints, and get starter GraphQL guidance before querying blockchain index data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Results include paid x402 query URLs that another wallet-enabled tool could call. <br>
Mitigation: Keep wallet and payment tools behind explicit approval before calling x402 URLs. <br>
Risk: Semantic search may need model assets that are unsuitable for strictly offline environments if not bundled. <br>
Mitigation: Avoid semantic search in offline deployments unless the embedding model is already bundled and available. <br>
Risk: Disabling registry database hash verification can allow stale or tampered registry data to load. <br>
Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY in normal agent-runtime configurations. <br>
Risk: Optional HTTP/SSE transport exposes local endpoints when enabled. <br>
Mitigation: Use the default stdio transport unless HTTP/SSE is needed, and enable HTTP/SSE only on trusted or firewalled networks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry) <br>
- [Project homepage](https://github.com/PaulieB14/subgraph-registry) <br>
- [Glama MCP server listing](https://glama.ai/mcp/servers/PaulieB14/subgraph-registry) <br>
- [The Graph](https://thegraph.com) <br>
- [Graph Protocol x402 client](https://www.npmjs.com/package/@graphprotocol/client-x402) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured MCP tool responses with subgraph metadata, query URLs, pricing metadata, reliability scores, schema details, and generated GraphQL examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns read-only discovery data; x402 URLs may require explicit wallet approval in downstream tools.] <br>

## Skill Version(s): <br>
0.8.22 (source: package.json and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
