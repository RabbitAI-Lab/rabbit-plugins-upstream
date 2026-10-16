## Description:

Guides agents in retrieving TripAdvisor location searches, nearby places, details, photos, and reviews through the Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to look up TripAdvisor places and reviews from a shell without running an MCP server, or to read public location details through a browser when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may expose a TripAdvisor API key when reading a local .env file or printing shell output.

Mitigation: Set TRIPADVISOR_API_KEY through your own shell or secret manager; do not print or disclose the key.

Risk: The browser fallback routes requests through a signed-in browser session.

Mitigation: Use a dedicated browser profile or enable the bridge only after reviewing its session access.

## Reference(s):

- [TripAdvisor API developer portal](https://www.tripadvisor.com/developers)
- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Browser fallback guidance](references/web-fallback.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Text or Markdown guidance with shell commands and JSON location results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location lookups; public-page fallback provides aggregate ratings but not individual review text.]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
