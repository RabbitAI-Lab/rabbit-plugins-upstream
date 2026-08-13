## Description:

Discover and filter 15,293 The Graph subgraphs by domain, network, protocol type, or natural language goal, with x402 query URLs for $0.01 USDC on Base per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agents use this skill to discover, rank, and inspect The Graph subgraphs before issuing GraphQL queries. It helps agents choose subgraphs by domain, network, protocol type, schema stability, reliability score, or natural-language goal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may follow x402 query URLs that require wallet-signed USDC payments.

Mitigation: Require explicit user approval before following query_url_x402 or signing any wallet payment.

Risk: Legacy query URLs require a The Graph Studio API key.

Mitigation: Use Studio API keys only when the user approves that path, and avoid exposing keys in prompts, logs, or shared outputs.

Risk: Optional HTTP/SSE mode exposes a local service endpoint.

Mitigation: Keep HTTP/SSE mode on trusted local networks or behind appropriate firewall controls.

Risk: Disabling registry hash verification can allow use of an unverified local database.

Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY unless deliberately rebuilding and validating the database locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)
- [Graph x402 client](https://www.npmjs.com/package/@graphprotocol/client-x402)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Configuration]

**Output Format:** [JSON tool responses with subgraph metadata, query URLs, pricing manifests, reliability scores, schema details, and query guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include x402 payment URLs, legacy Studio API-key URL templates, local HTTP/SSE endpoint information, and example GraphQL queries.]

## Skill Version(s):

0.8.28 (source: release evidence, package.json, server.json, OpenAPI)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
