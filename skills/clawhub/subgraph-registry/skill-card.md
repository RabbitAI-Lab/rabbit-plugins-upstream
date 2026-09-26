## Description:

Helps agents discover and compare classified subgraphs on The Graph, with optional schema inspection and GraphQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this MCP server to find suitable subgraphs by network, topic, activity, and reliability before optionally inspecting schemas or running GraphQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installs can fetch a different release.

Mitigation: Install the pinned version specified in SKILL.md.

Risk: Exposing HTTP mode with a Graph Studio API key can allow authenticated schema or query calls that consume API quota.

Mitigation: Keep HTTP mode on a trusted interface and restrict access to the keyed service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/paulieb14/skills/subgraph-registry)
- [Project homepage listed in skill metadata](https://github.com/PaulieB14/subgraph-registry)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery results include query volume and reliability; schema inspection and querying are opt-in.]

## Skill Version(s):

0.10.5 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
