## Description:

Find TripAdvisor hotels, restaurants, and attractions, including nearby places, ratings, reviews, photos, and listing details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use this skill to find and compare hotels, restaurants, and attractions using TripAdvisor listings, ratings, reviews, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted third-party MCP package could expose the local environment.

Mitigation: Install only if you trust the @chrischall/tripadvisor-mcp package.

Risk: The Terra API key is stored in MCP configuration and travel lookups are sent to TripAdvisor/Terra; optional browser lookups use public TripAdvisor pages.

Mitigation: Protect the API key, prefer project-scoped configuration when possible, and avoid sending sensitive trip details.

## Reference(s):

- [ClawHub tripadvisor release](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or text with place details, ratings, reviews, and photo links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; search and review results can be paginated.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
