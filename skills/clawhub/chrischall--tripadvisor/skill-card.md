## Description:

Helps agents find hotels, restaurants, and attractions and retrieve TripAdvisor place details, ratings, reviews, and photos through the Terra API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to find and compare places to stay, eat, and visit, including nearby listings, ratings, reviews, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external MCP package requires trusting its publisher.

Mitigation: Verify that you trust the package before installation.

Risk: TripAdvisor lookups make network requests and require a Terra API key; an optional browser bridge may also be used.

Mitigation: Store a valid Terra API key only in the MCP configuration and enable the browser bridge only if needed.

## Reference(s):

- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include place links, review excerpts, and photo URLs.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
