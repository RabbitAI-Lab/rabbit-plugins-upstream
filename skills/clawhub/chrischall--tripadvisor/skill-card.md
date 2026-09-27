## Description:

Helps agents find and compare hotels, restaurants, and attractions using TripAdvisor place listings, ratings, photos, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use this skill to locate and compare hotels, restaurants, and attractions, including nearby places, ratings, photos, and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires running a third-party MCP package.

Mitigation: Review and trust the package before installing or running it.

Risk: TripAdvisor searches and precise locations may be sent to external services along with requests authenticated by an API key.

Mitigation: Keep the API key private and avoid sharing sensitive precise locations unless that disclosure is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown travel recommendations and place details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include location details, ratings, review excerpts, photo links, and source URLs.]

## Skill Version(s):

1.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
