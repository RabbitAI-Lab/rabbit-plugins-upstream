## Description:

Provides read-only TripAdvisor place searches, details, reviews, and photos through the Terra API and an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and their agents use this skill to find hotels, restaurants, and attractions, compare places, and retrieve TripAdvisor ratings, reviews, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external MCP package and TripAdvisor API sends searches, location IDs, and coordinates to external services.

Mitigation: Install the package only if its external-service use is acceptable, and avoid sending precise sensitive locations unless needed.

Risk: The setup requires a TripAdvisor Terra API key.

Mitigation: Keep the key scoped to TripAdvisor and supply it through the MCP server environment rather than sharing it in requests.

## Reference(s):

- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor MCP package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration guidance, Shell commands]

**Output Format:** [Markdown guidance and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only place data; compact or full views for supported tools.]

## Skill Version(s):

1.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
