## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-planning agents use this skill to search TripAdvisor locations, compare hotels, restaurants, and attractions, and retrieve ratings, details, photos, and reviews through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended setup runs an unpinned third-party MCP package that can change over time.

Mitigation: Pin the npm package to a reviewed version or use a specific reviewed commit before enabling the server.

Risk: The MCP server receives a TripAdvisor API key.

Mitigation: Use a dedicated revocable API key, avoid shared production keys in plaintext config, and grant only the access needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package: @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe MCP setup, environment variables, TripAdvisor lookup workflows, and read-only API results.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
