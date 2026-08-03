## Description: <br>
Discover and filter 15,252 The Graph subgraphs by domain, network, protocol type, or natural language goal; each result includes an x402 query URL for $0.01 USDC on Base with no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this MCP server to choose reliable The Graph subgraphs, inspect schema and classification details, and receive x402 or legacy query endpoints before issuing GraphQL requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can recommend paid x402 query paths that spend $0.01 USDC on Base per query. <br>
Mitigation: Require explicit approval before an agent uses a wallet or x402 client to authorize payment. <br>
Risk: Registry or model data may be downloaded if bundled files are missing. <br>
Mitigation: For offline or locked-down runtimes, pre-bundle the registry and model data and block fallback downloads. <br>
Risk: HTTP/SSE mode exposes local server endpoints when explicitly enabled. <br>
Mitigation: Keep the default stdio transport unless HTTP is required, and bind HTTP/SSE only in trusted local or firewalled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry) <br>
- [Project homepage](https://github.com/PaulieB14/subgraph-registry) <br>
- [Glama MCP server page](https://glama.ai/mcp/servers/PaulieB14/subgraph-registry) <br>
- [The Graph](https://thegraph.com) <br>
- [Graph Protocol x402 client](https://www.npmjs.com/package/@graphprotocol/client-x402) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance, configuration] <br>
**Output Format:** [MCP tool responses as JSON with text guidance, query URLs, and optional pricing manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include x402 pricing manifests, legacy The Graph gateway URLs, reliability scores, schema details, and local transport configuration guidance.] <br>

## Skill Version(s): <br>
0.8.25 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
