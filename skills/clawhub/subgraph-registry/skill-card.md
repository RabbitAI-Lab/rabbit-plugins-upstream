## Description:

Helps agents find and compare indexed subgraphs, with optional schema lookup and GraphQL query execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to discover and compare subgraphs across networks before optionally fetching schemas or querying The Graph with a Studio API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP/SSE access can expose API-key-backed query tools without authentication if reachable from a public or local network.

Mitigation: Prefer local stdio and keyless discovery; if HTTP/SSE is required with a key, enforce authentication, rate limits, and firewall restrictions.

Risk: Unpinned installations or disabling registry verification can introduce unreviewed code or data.

Mitigation: Pin the package version and leave registry integrity verification enabled in agent runtimes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage (listed in skill metadata)](https://github.com/PaulieB14/subgraph-registry)
- [The Graph Studio API keys](https://thegraph.com/studio/apikeys/)

## Skill Output:

**Output Type(s):** [Text, JSON, GraphQL query results]

**Output Format:** [Structured MCP tool responses with subgraph matches, schema information, or query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery does not execute GraphQL; schema and query execution are opt-in.]

## Skill Version(s):

0.10.9 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
