## Description: <br>
Discover and filter 15,254 The Graph subgraphs by domain, network, protocol type, or natural language goal, with x402 query URLs included in results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to discover, rank, and inspect The Graph subgraphs before querying them. It helps agents choose subgraphs by domain, network, protocol type, reliability, schema details, and x402 or legacy query endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Returned x402 endpoints can lead to paid GraphQL queries if connected wallet or payment tools are allowed to act automatically. <br>
Mitigation: Require explicit confirmation for wallet signing and payment tools before any x402 query is retried with payment. <br>
Risk: Semantic search can require model assets and may be unsuitable for strict air-gapped environments if those assets are not bundled. <br>
Mitigation: Pre-bundle the model or avoid semantic_search_subgraphs in air-gapped deployments. <br>
Risk: The optional HTTP/SSE transport exposes local endpoints when enabled. <br>
Mitigation: Use the default stdio transport unless remote access is required, and bind HTTP/SSE only in trusted or firewalled environments. <br>
Risk: Unpinned npm execution can install a later package version with different behavior. <br>
Mitigation: Pin the npm version, for example subgraph-registry-mcp@0.8.23, before use in an agent runtime. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry) <br>
- [Project homepage from metadata.clawdis](https://github.com/PaulieB14/subgraph-registry) <br>
- [The Graph Network](https://thegraph.com) <br>
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/) <br>
- [Graph Protocol x402 client](https://www.npmjs.com/package/@graphprotocol/client-x402) <br>
- [Transformers.js](https://github.com/xenova/transformers.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [MCP tool responses with JSON-compatible result data, URLs, and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include paid x402 query URLs, legacy API-key URLs, reliability scores, schema details, and example GraphQL query instructions.] <br>

## Skill Version(s): <br>
0.8.23 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
