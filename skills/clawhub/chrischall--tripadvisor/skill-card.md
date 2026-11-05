## Description:

Find and compare TripAdvisor hotels, restaurants, and attractions, including ratings, reviews, photos, and nearby options, through the Terra API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel planners use this skill to find places and compare hotels, restaurants, and attractions using TripAdvisor listings, ratings, reviews, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The TripAdvisor API key could be exposed through shared configuration or repositories.

Mitigation: Keep the key out of shared repositories and protect its configuration.

Risk: Search inputs are sent to TripAdvisor and API usage may incur charges.

Mitigation: Use approximate locations when sufficient and check API charges.

Risk: The external server and optional browser bridge are unverified.

Mitigation: Prefer a pinned, reviewed server version and enable the browser bridge only when needed.

## Reference(s):

- [TripAdvisor Terra API developer portal](https://www.tripadvisor.com/developers)
- [tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text summaries and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include place details, ratings, review summaries, photo links, and listing URLs.]

## Skill Version(s):

1.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
