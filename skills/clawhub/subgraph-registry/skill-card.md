## Description:

Use to discover The Graph subgraphs by chain, protocol, entity or contract and turn a goal into a bounded GraphQL query. Bring-your-own Studio key (set up by a human operator) for execution; discovery never executes queries or signs payments, and x402 is an explicitly paid external option.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and data analysts can use the MCP server to discover and inspect The Graph subgraphs, then prepare bounded GraphQL queries from a goal. Live schema checks and query execution are optional and require a Studio key managed by the operator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a benign verdict with medium confidence, but only 10 of 23 components were fully inspected.

Mitigation: Review the remaining components and the selected release before installation; the verdict does not establish that every component is safe.

Risk: The security guidance notes unpinned npx references can resolve to a different release.

Mitigation: Install the reviewed version explicitly, such as subgraph-registry-mcp@0.13.3.

Risk: Opt-in gateway tools use the operator's Studio key, so exposing the optional listener remotely can expose those capabilities.

Mitigation: Keep the key in the host secret store and require a separate bearer token for non-loopback listener binds.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage (Clawdis metadata)](https://github.com/PaulieB14/subgraph-registry)
- [The Graph supported networks](https://thegraph.com/docs/en/supported-networks/)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [JSON, GraphQL query, Guidance]

**Output Format:** [Structured MCP responses with JSON data and GraphQL query text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery uses the bundled registry snapshot. Live schema checks and query execution are opt-in and require an operator-managed Studio key; the server does not automatically make paid x402 requests.]

## Skill Version(s):

0.13.3 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
