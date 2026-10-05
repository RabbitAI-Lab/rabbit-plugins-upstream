## Description:

Helps agents discover classified subgraphs on The Graph and optionally inspect schemas or execute GraphQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to find and compare subgraphs, inspect their schemas, and explicitly run GraphQL queries when credentials are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remotely reachable HTTP/SSE clients could use credential-backed query tools and consume API quota.

Mitigation: Use stdio or loopback-only HTTP locally; require authentication for remote access and avoid exposing a server configured with gateway API keys.

Risk: Unreviewed updates can change the skill's behavior.

Mitigation: Install a pinned, reviewed version.

Risk: Using the optional x402 client flow can spend real funds.

Mitigation: Require explicit consent and spending limits before signing payments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage (listed in skill metadata)](https://github.com/PaulieB14/subgraph-registry)
- [The Graph](https://thegraph.com)

## Skill Output:

**Output Type(s):** [Text, Code]

**Output Format:** [Structured JSON results, GraphQL schemas and example queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery does not automatically execute queries or initiate payments.]

## Skill Version(s):

0.10.7 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
