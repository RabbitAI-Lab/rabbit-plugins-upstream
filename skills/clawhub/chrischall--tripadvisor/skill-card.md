## Description:

Helps agents find hotels, restaurants, and attractions and retrieve TripAdvisor ratings, reviews, photos, and nearby places through read-only lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and other agents use the skill to compare places to stay or eat, discover attractions, and retrieve place details, ratings, reviews, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party package requires trusting its publisher.

Mitigation: Verify that the package is trusted before installation.

Risk: A TripAdvisor Terra API key is needed for API lookups and could be exposed through an unintended configuration.

Mitigation: Use a valid Terra key only in the MCP configuration you intend to use and keep the key private.

Risk: The MCP registration remains active until its configuration entry is removed.

Mitigation: Remove the MCP entry when access is no longer needed.

## Reference(s):

- [ClawHub tripadvisor skill](https://clawhub.ai/chrischall/skills/tripadvisor)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include place ratings, reviews, listing URLs, and photo links.]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
