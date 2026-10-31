## Description:

Find and compare hotels, restaurants, and attractions using TripAdvisor ratings, reviews, photos, and nearby search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel planners can find nearby or named hotels, restaurants, and attractions, then review their ratings, details, photos, and traveler reviews to compare options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests send the supplied search terms and location to TripAdvisor.

Mitigation: Use a city or approximate location when it is sufficient for the search.

Risk: The Terra API key and optional browser bridge grant access to external services or a browser session.

Mitigation: Protect the API key, review and preferably pin the external package version, and enable the browser bridge only when browser-session access is intended.

## Reference(s):

- [TripAdvisor Terra API developer portal](https://www.tripadvisor.com/developers)
- [@chrischall/tripadvisor-mcp package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [TripAdvisor place listings, ratings, reviews, photo links, and concise natural-language comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses are the default for supported tools; list results can be paginated.]

## Skill Version(s):

1.1.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
