## Description:

Helps agents discover and compare classified subgraphs on The Graph, with optional schema inspection and GraphQL querying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use the registry to find suitable subgraphs by topic, chain, entity, semantic goal, reliability, and query volume. They can then inspect schemas or run GraphQL queries when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional schema and GraphQL requests can access The Graph gateway when invoked.

Mitigation: Leave API keys unset for discovery-only use; if enabling queries, provide a limited API key.

Risk: Exposing the optional HTTP/SSE service can make its endpoints reachable to others.

Mitigation: Protect HTTP access with authentication before exposing the service.

Risk: An external x402 client can authorize USDC payments for GraphQL queries.

Mitigation: Use a separate client and require explicit spending authorization for wallet payments.

Risk: A missing registry database may be fetched at startup.

Mitigation: Keep the pinned database hash verification enabled.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Source repository (metadata homepage)](https://github.com/PaulieB14/subgraph-registry)
- [Graph Studio API keys](https://thegraph.com/studio/apikeys/)
- [Official subgraph MCP project](https://github.com/graphops/subgraph-mcp)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON tool responses containing registry records, schema details, or optional GraphQL results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery is read-only; schema inspection and GraphQL execution are opt-in.]

## Skill Version(s):

0.10.13 (source: server-resolved release metadata, artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
