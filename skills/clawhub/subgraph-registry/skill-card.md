## Description:

Helps agents discover and compare classified subgraphs on The Graph, with optional schema inspection and GraphQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use the local registry to find and compare subgraphs by chain, topic, usage, and reliability. With an API key, they can optionally inspect live schemas and execute GraphQL queries through The Graph gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An HTTP/SSE listener exposed beyond loopback may allow unauthenticated use of credential-backed query tools and consume the operator's Graph Studio API quota.

Mitigation: Keep HTTP/SSE on a trusted loopback or firewalled network; if exposed, protect /sse and /messages with an authenticating proxy and rate limits.

Risk: Unpinned package installation can run a release that has not been reviewed.

Mitigation: Install in a controlled environment using the pinned version in SKILL.md rather than unpinned README npx examples.

## Reference(s):

- [ClawHub release](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Declared project homepage](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured tool responses and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery is local; live schema inspection and queries are opt-in and require a gateway API key.]

## Skill Version(s):

0.10.8 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
