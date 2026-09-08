## Description:

TripAdvisor provides read-only travel lookup through the Terra API via MCP for finding and comparing hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and agent users use this skill to search TripAdvisor locations, compare places to stay or eat, and retrieve read-only place details, reviews, ratings, photos, and nearby attractions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended setup can run an unpinned third-party MCP package.

Mitigation: Pin the MCP package version or a specific source commit before installing or running it.

Risk: The TripAdvisor API key may be stored in plaintext configuration.

Mitigation: Keep the API key out of committed or shared project files and limit the MCP server to only the filesystem and environment access it needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developers](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown or text with JSON MCP tool inputs and responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor Terra API lookup results; compact views are available for several tools.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
