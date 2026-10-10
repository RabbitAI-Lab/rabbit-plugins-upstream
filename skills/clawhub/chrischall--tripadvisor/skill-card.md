## Description:

Helps agents find hotels, restaurants, and attractions and summarize TripAdvisor ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use this skill to research and compare hotels, restaurants, and attractions through TripAdvisor location data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external MCP package requires trusting code outside this skill.

Mitigation: Review the package and its publisher before installation.

Risk: The MCP server requires a TripAdvisor API key for Terra lookups.

Mitigation: Provide the key only to a trusted server and keep it out of shared files and responses.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include place details, ratings, review summaries, photo links, and nearby suggestions.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
