## Description:

TripAdvisor provides travel lookups through the Terra API via MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search TripAdvisor travel data, compare places to stay or eat, and retrieve location details, photos, and reviews through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires running a third-party MCP package and storing a TripAdvisor Terra API key in MCP configuration.

Mitigation: Confirm the package source and configure the API key only in trusted local MCP settings or a secret-managed environment.

Risk: The optional browser-bridge tool may route requests through an open TripAdvisor browser session.

Mitigation: Use the browser bridge only when that routing behavior is acceptable, and prefer the Terra API path when an API key is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package: @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor Developers](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP tool recommendations, setup snippets, and travel lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include TripAdvisor location IDs, ratings, review summaries, photo URLs, addresses, and configuration examples.]

## Skill Version(s):

0.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
