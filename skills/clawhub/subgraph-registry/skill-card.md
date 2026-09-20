## Description:

Same abilities as graphops/subgraph-mcp with better discovery. Search 15,370+ classified subgraphs; real 30-day query volume on every hit; opt-in schema and execute under the official tool names. Discovery tools never auto-query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent builders use this skill to discover classified subgraphs on The Graph Network, compare reliability and query-volume signals, inspect cached schemas, and optionally execute GraphQL queries when credentials are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP/SSE mode can expose a configured Graph API key to unauthenticated clients who can spend query quota.

Mitigation: Use local stdio discovery by default, or place HTTP/SSE behind authentication, a firewall, and rate limits before setting Graph API keys.

Risk: Unpinned package execution or unreviewed upgrades can change behavior in autonomous-agent deployments.

Mitigation: Pin the npm package version and review upgrades before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project Homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Network](https://thegraph.com)
- [The Graph Studio API Keys](https://thegraph.com/studio/apikeys/)
- [Graph Protocol x402 Client](https://www.npmjs.com/package/@graphprotocol/client-x402)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON tool results and Markdown guidance with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery results are local by default; execute and live-schema actions are opt-in and require configured credentials.]

## Skill Version(s):

0.10.3 (source: package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
