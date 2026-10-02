## Description:

Helps agents find and compare hotels, restaurants, and attractions using TripAdvisor location details, ratings, reviews, and photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to look up places, compare ratings and reviews, and find nearby hotels, restaurants, and attractions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server receives the TripAdvisor Terra API key and makes network requests for travel data.

Mitigation: Verify the package publisher before installing and provide only an API key you are comfortable sharing with the server.

Risk: Setup changes local MCP configuration; the optional browser bridge can access public TripAdvisor pages when enabled.

Mitigation: Review configuration changes and enable the browser bridge only when needed.

## Reference(s):

- [ClawHub tripadvisor skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include place details, ratings, review text, photo URLs, and setup guidance.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
