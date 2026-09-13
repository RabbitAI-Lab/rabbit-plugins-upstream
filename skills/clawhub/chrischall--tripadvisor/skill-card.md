## Description:

Provides TripAdvisor travel data via the Terra API for finding and comparing hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search TripAdvisor-backed travel listings and retrieve place details, ratings, reviews, and photos for trip planning and local discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup asks users to run an unpinned external npm package.

Mitigation: Pin the npm package version or source commit and inspect the package before running it.

Risk: The Terra API key may be stored in persistent MCP configuration and can carry quota or billing impact.

Mitigation: Keep the key out of shared project files, restrict configuration file permissions, and monitor or limit API usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [Text, API calls, Configuration guidance]

**Output Format:** [Markdown guidance with structured travel data returned from MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TripAdvisor Terra API key for Terra endpoints; several list and review tools default to compact responses.]

## Skill Version(s):

0.6.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
