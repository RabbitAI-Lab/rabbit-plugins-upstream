## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-planning agents use this skill to query TripAdvisor Terra data through an MCP server for place search, details, photos, reviews, and nearby recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP server package receives the TripAdvisor API key through environment configuration.

Mitigation: Review the npm or source package before installation, pin a known version, and use a key with the least privileges and quota suitable for the deployment.

Risk: Agent tool calls can consume TripAdvisor API quota.

Mitigation: Use a dedicated Terra API key with quota limits and monitor usage for the environment where the skill is installed.

## Reference(s):

- [TripAdvisor Developers](https://www.tripadvisor.com/developers)
- [@chrischall/tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [ClawHub tripadvisor skill page](https://clawhub.ai/chrischall/skills/tripadvisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON MCP configuration snippets, bash setup commands, and structured travel data returned through MCP tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor travel data; selected tools support compact or full response views.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
