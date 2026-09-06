## Description:

Same abilities as graphops/subgraph-mcp with better discovery. Search 15,000+ classified subgraphs; real 30-day query volume on every hit; opt-in schema and execute under the official tool names. Discovery tools never auto-query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to discover, compare, and select subgraphs on The Graph Network before deciding whether to inspect schemas or execute GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE mode can expose a local server, and risk increases if it is reachable while The Graph API keys are configured.

Mitigation: Use the default stdio transport for local discovery; if HTTP/SSE is enabled, keep it on loopback or protect it with authentication and network controls.

Risk: Runtime may download registry or embedding assets from GitHub or Hugging Face if bundled files are missing.

Mitigation: Install a pinned version, keep bundled data/model files present for controlled deployments, and rely on the pinned registry hash verification before loading data.

Risk: Opt-in query tools can send GraphQL requests to The Graph gateway when credentials are set.

Mitigation: Use discovery tools first, invoke execute/schema tools only when needed, and manage THE_GRAPH_STUDIO_API_KEY or GATEWAY_API_KEY in the runtime environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [graphops/subgraph-mcp](https://github.com/graphops/subgraph-mcp)
- [The Graph Network](https://thegraph.com)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Guidance]

**Output Format:** [Structured MCP tool responses with JSON fields, GraphQL query text, query URLs, and status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery tools return local registry results; schema and execute tools are opt-in and may require The Graph credentials.]

## Skill Version(s):

0.9.15 (source: package.json, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
