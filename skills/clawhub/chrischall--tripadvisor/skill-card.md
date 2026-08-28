## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and travel-focused agent users use this skill to connect an agent to TripAdvisor Terra API data for searching places and retrieving listing details, photos, and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the referenced third-party MCP package executes non-NVIDIA code.

Mitigation: Install only from trusted package sources and review or scan the package before deployment.

Risk: The integration requires a TripAdvisor Terra API key for API-backed tools.

Mitigation: Store the key in environment configuration, limit access to it, and monitor usage against the active plan.

Risk: The optional browser bridge reads TripAdvisor pages through the user's open TripAdvisor tab.

Mitigation: Enable the bridge only when needed and use it with the intended TripAdvisor pages.

## Reference(s):

- [tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [tripadvisor-mcp GitHub repository](https://github.com/chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TripAdvisor Terra API key for API-backed tools; optional browser bridge can retrieve limited public page details without an API key.]

## Skill Version(s):

0.3.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
