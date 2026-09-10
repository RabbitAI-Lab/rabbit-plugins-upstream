## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, and attractions, looking up ratings, reviews, and photos, comparing places, and finding what is nearby.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to TripAdvisor Terra API data for travel planning, place comparison, and location lookup workflows. It supports read-only searches and details for hotels, restaurants, attractions, photos, and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned third-party MCP package that receives a TripAdvisor API key.

Mitigation: Pin the MCP package to a reviewed version or commit before installation and review the package before use.

Risk: A real TripAdvisor API key could be exposed if committed in project configuration or shared agent settings.

Mitigation: Keep the API key out of source control, use a dedicated TripAdvisor key, and apply quota or billing controls.

Risk: The MCP server needs network access and may be installed from a third-party package source.

Mitigation: Run the server with only the filesystem and network access needed for TripAdvisor data retrieval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package: @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Source repository referenced by artifact](https://github.com/chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup instructions, environment variable guidance, tool selection guidance, and read-only travel data returned through the MCP server.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
