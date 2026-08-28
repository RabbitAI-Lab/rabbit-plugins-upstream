## Description:

Query TripAdvisor location data from a shell using curl against the Terra REST API, with a browser-bridge fallback for public location details when an API key is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to retrieve TripAdvisor search, nearby, location details, photos, and reviews data without running the MCP server. It is useful for scripted lookups, direct API calls, and fallback extraction of public location details when a Terra API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-based fpx fallback can save TripAdvisor page HTML under /tmp/ta-location.html, and that HTML may include personalized page content.

Mitigation: Prefer the Terra API key flow when possible; when using fpx, use a dedicated TripAdvisor browser profile if practical and delete /tmp/ta-location.html after parsing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [TripAdvisor Developer Portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only API lookup recipes and parsing guidance; no TripAdvisor write operations.]

## Skill Version(s):

0.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
