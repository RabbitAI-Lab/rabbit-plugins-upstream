## Description:

Provides TripAdvisor Terra API travel data through an MCP server for finding and inspecting hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-planning agents use this skill to search TripAdvisor places, compare hotels, restaurants, and attractions, and retrieve location details, reviews, and photos through MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the referenced npm package or source repository can execute third-party code in the agent environment.

Mitigation: Confirm the package and repository are trusted before installation.

Risk: TripAdvisor Terra requests require an API key and may incur usage or billing under the configured plan.

Mitigation: Use an API key with appropriate billing limits and monitor call volume.

Risk: Travel lookup requests are sent to TripAdvisor, and the optional browser bridge can fetch public TripAdvisor page details.

Mitigation: Avoid sending sensitive user data in lookup queries and enable the browser bridge only when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package listed in skill artifact](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [Source repository listed in skill artifact](https://github.com/chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only travel lookup guidance and results; may include API-backed place details, reviews, photos, and diagnostic information.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
