## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query TripAdvisor Terra travel data through an MCP server, including place search, nearby search, listing details, photos, reviews, and diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external MCP package and source outside NVIDIA control.

Mitigation: Install only after reviewing and trusting the referenced package or source.

Risk: A TripAdvisor Terra API key must be placed in MCP configuration.

Mitigation: Use a valid Terra key, restrict access to configuration files, and rotate the key if it may have been exposed.

Risk: API calls may count against a TripAdvisor plan, and cached responses may remain in memory while the server runs.

Mitigation: Monitor API usage and configure or disable cache TTLs according to the deployment's privacy and cost requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor)
- [npm package @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Referenced source repository](https://github.com/chrischall/tripadvisor-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor Terra data responses depend on the configured MCP server, API key validity, pagination, and cache settings.]

## Skill Version(s):

0.4.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
