## Description:

Discover and filter 15,324 The Graph subgraphs by domain, network, protocol type, or natural language goal, with x402 query URLs for $0.01 USDC on Base per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP server to discover relevant The Graph subgraphs, inspect schemas and reliability signals, and obtain query instructions before asking an agent to query blockchain data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned npm package can pull a newer release than the reviewed version.

Mitigation: Install the pinned package version, for example subgraph-registry-mcp@0.8.30.

Risk: Enabling HTTP or SSE transport exposes a local listener and MCP endpoints.

Mitigation: Use the default stdio transport for local agent use, and only enable HTTP/SSE in trusted or firewalled environments.

Risk: Bypassing registry hash verification can allow an unexpected or tampered database to load.

Mitigation: Do not set SUBGRAPH_REGISTRY_SKIP_VERIFY in normal deployments.

Risk: Semantic search may need network access if the embedding model is not bundled in the runtime.

Mitigation: Avoid semantic_search_subgraphs in strictly offline deployments unless the model is pre-bundled locally.

Risk: x402 query URLs can trigger paid blockchain query flows when an agent has signing access.

Mitigation: Apply wallet, spending, and approval controls before allowing autonomous agents to sign paid x402 requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)
- [Graph Studio API keys](https://thegraph.com/studio/apikeys/)
- [@graphprotocol/client-x402](https://www.npmjs.com/package/@graphprotocol/client-x402)
- [README](artifact/README.md)
- [OpenAPI specification](artifact/openapi.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON tool results, Markdown guidance, shell commands, query URLs, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP responses may include reliability scores, schema details, x402 pricing manifests, and step-by-step query instructions.]

## Skill Version(s):

0.8.30 (source: evidence release, package.json, server.json, OpenAPI)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
