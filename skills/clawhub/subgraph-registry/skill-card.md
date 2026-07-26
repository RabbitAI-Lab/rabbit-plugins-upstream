## Description: <br>
Discover and filter 15,500+ The Graph subgraphs by domain, network, protocol type, or natural language goal, with x402 query URLs for $0.01 USDC on Base per call and no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this MCP server to discover, rank, and inspect The Graph subgraphs before querying them. It returns structured subgraph metadata, schema details, reliability signals, query instructions, and x402 or legacy gateway URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill returns x402 query links that can lead to paid wallet transactions if an agent follows them with signing authority. <br>
Mitigation: Require explicit approval before signing x402 payments or using wallet credentials, and limit autonomous use of query_url_x402 links. <br>
Risk: The runtime may download verified registry or model assets. <br>
Mitigation: Pin the npm package version, allow network access only to approved sources, and keep registry hash verification enabled. <br>
Risk: Optional HTTP/SSE mode exposes local endpoints when enabled. <br>
Mitigation: Use stdio by default, and enable HTTP/SSE only in trusted or firewalled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry) <br>
- [Project homepage](https://github.com/PaulieB14/subgraph-registry) <br>
- [The Graph](https://thegraph.com) <br>
- [x402 client package](https://www.npmjs.com/package/@graphprotocol/client-x402) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, configuration, guidance] <br>
**Output Format:** [MCP tool responses and optional HTTP JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns subgraph classifications, reliability scores, schema details, query URLs, pricing manifests, and query guidance.] <br>

## Skill Version(s): <br>
0.8.19 (source: package.json, server.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
