## Description:

TripAdvisor provides travel lookup through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places via the TripAdvisor Terra API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners, support agents, and developers use this skill to query TripAdvisor listings, compare hotels, restaurants, and attractions, and retrieve details, reviews, photos, and nearby options through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server makes network requests to TripAdvisor and may consume Terra API quota.

Mitigation: Use a TripAdvisor Terra API key with appropriate limits and monitor quota usage before relying on high-volume workflows.

Risk: A missing, inactive, or legacy API key can prevent Terra API lookups from returning results.

Mitigation: Verify that the configured key is a valid active Terra key before deployment or time-sensitive travel planning.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor Developer Portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples; MCP tool results are structured TripAdvisor travel data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TripAdvisor Terra API key for Terra endpoints; compact views are the default for supported lookup tools.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
