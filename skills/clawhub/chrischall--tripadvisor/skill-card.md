## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, and attractions, looking up ratings, reviews, and photos, comparing places to stay or eat, and finding what is near a location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route travel-planning requests through a TripAdvisor MCP server, including place search, nearby discovery, location details, photos, and traveler reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill requires executing the third-party @chrischall/tripadvisor-mcp package through MCP.

Mitigation: Review the package source and release before installation when stronger assurance is required.

Risk: The skill requires a TripAdvisor Terra API key in MCP configuration.

Mitigation: Store only the required key in the MCP environment configuration and rotate it if the configuration is exposed.

Risk: The optional browser bridge can route lookups through a signed-in browser tab.

Mitigation: Keep the browser bridge disabled unless that behavior is explicitly desired.

## Reference(s):

- [Tripadvisor ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [@chrischall/tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [tripadvisor-mcp source repository](https://github.com/chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides setup and use of read-only TripAdvisor MCP tools that return travel search, detail, photo, and review data.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
