## Description:

Same abilities as graphops/subgraph-mcp with better discovery. Search 15,452+ classified subgraphs; real 30-day query volume on every hit; opt-in schema and execute under the official tool names. Discovery tools never auto-query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use the MCP server to find and compare classified subgraphs on The Graph Network, using network, domain, schema, and activity signals. They can inspect schemas or run a GraphQL query when explicitly requested and configured with credentials or an independently approved payment flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external x402 client can make paid queries, with payment handled by the caller.

Mitigation: Approve payments separately before using an x402 client; discovery does not query or pay automatically.

Risk: HTTP/SSE hosting can expose a keyed instance to callers who can reach it.

Mitigation: Use stdio for keyed instances or put HTTP access behind authentication and trusted network controls.

Risk: The bundled database, model contents, and resolved dependencies were unavailable for verification, and filtered schema-stability results can be misleading.

Mitigation: Use the pinned installation, keep database hash verification enabled, and review schema-stability results with the underlying subgraph data.

## Reference(s):

- [Project homepage and documentation](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Network](https://thegraph.com/)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Structured data (JSON), GraphQL query results, Guidance]

**Output Format:** [Structured MCP responses and GraphQL response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery results include subgraph metadata and query routes; schema inspection and query execution are opt-in.]

## Skill Version(s):

0.10.16 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
