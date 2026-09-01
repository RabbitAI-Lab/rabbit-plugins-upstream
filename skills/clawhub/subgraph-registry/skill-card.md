## Description:

Discover and filter 15,306 The Graph subgraphs by domain, network, protocol type, or natural language goal, with x402 query URLs for $0.01 USDC on Base per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

External developers and agents use this skill to discover suitable The Graph subgraphs, inspect metadata and query options, and choose an API-key or x402 route before running GraphQL queries elsewhere.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode can expose MCP endpoints if enabled on an untrusted interface.

Mitigation: Use the default stdio transport unless remote access is required, and bind HTTP/SSE only on trusted or firewalled interfaces.

Risk: x402 query routes can spend USDC when an agent submits or retries paid GraphQL requests.

Mitigation: Require explicit approval, spending caps, and wallet allowlists before enabling autonomous paid queries.

Risk: Strictly offline environments may fail if the registry database or semantic-search model is not already bundled.

Mitigation: Pre-bundle registry.db and the embedding model, or avoid semantic_search_subgraphs in air-gapped deployments.

Risk: Subgraph discovery scores can be age-biased and do not guarantee that a selected subgraph is the best fit for a live query.

Mitigation: Review returned maturity, reliability context, and emerging-result caveats before recommending a subgraph.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Publisher profile](https://clawhub.ai/user/paulieb14)
- [Project homepage from ClawHub metadata](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [Graph Studio API keys](https://thegraph.com/studio/apikeys/)
- [@graphprotocol/client-x402](https://www.npmjs.com/package/@graphprotocol/client-x402)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSON tool results with subgraph metadata, starter GraphQL queries, query URLs, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery output; x402 query routes can require paid USDC transactions outside the skill.]

## Skill Version(s):

0.9.12 (source: evidence release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
