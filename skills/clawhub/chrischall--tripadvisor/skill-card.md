## Description:

Helps agents find and compare hotels, restaurants, and attractions using TripAdvisor location details, ratings, reviews, and photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use this skill to search nearby places and compare TripAdvisor ratings, reviews, and photos for hotels, restaurants, and attractions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration requires an external package and stores a TripAdvisor API key in agent configuration.

Mitigation: Confirm the package is trusted before installation and protect the API key in configuration.

Risk: Travel queries are sent to TripAdvisor, and optional browser access may read public TripAdvisor pages.

Mitigation: Avoid including sensitive personal information in searches and enable the browser bridge only when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown with place details and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only place data; search results and reviews may be paginated.]

## Skill Version(s):

1.1.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
