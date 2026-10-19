## Description:

Discovers and ranks classified subgraphs on The Graph Network, with optional schema lookup and GraphQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use the registry to find and compare subgraphs by chain, topic, activity, and reliability before optionally inspecting schemas or querying The Graph gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installs or vulnerable dependencies may introduce supply-chain risk.

Mitigation: Install a pinned version and review dependency advisories before production use.

Risk: Exposing the optional HTTP/SSE endpoint to untrusted clients may allow unintended tool access.

Mitigation: Keep HTTP/SSE disabled unless needed and expose it only on trusted networks.

Risk: Clients with access to a configured Graph gateway key can invoke queries and consume quota.

Mitigation: Leave gateway keys unset for discovery-only use; restrict access to keyed tools when enabled.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage (listed in skill metadata)](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery returns ranked subgraph metadata; live queries require a configured gateway key.]

## Skill Version(s):

0.10.10 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
