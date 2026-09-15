## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, details, and nearby places after the required server and API key are configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search TripAdvisor places, compare hotels, restaurants, and attractions, and retrieve ratings, reviews, photos, addresses, and nearby-place data through an MCP-backed TripAdvisor Terra API integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended setup runs an unpinned third-party package that can access a TripAdvisor API key.

Mitigation: Review the package source before installing, pin to a reviewed version or commit where possible, and use a dedicated TripAdvisor API key with tight quota and billing limits.

Risk: MCP configuration may expose a TripAdvisor API key if committed or shared.

Mitigation: Keep MCP configuration files containing secrets out of version control and remove the server entry when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package: @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include MCP server setup, environment variable configuration, and TripAdvisor lookup workflows.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
