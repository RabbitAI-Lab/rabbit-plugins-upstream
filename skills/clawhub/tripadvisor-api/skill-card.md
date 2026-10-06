## Description:

Helps agents look up TripAdvisor locations, photos, and reviews through the read-only Terra API, with a browser-based fallback for basic location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and developers use this skill to search for places and retrieve TripAdvisor location details, photos, and reviews without running an MCP server. A paired browser can retrieve basic public location details when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles a TripAdvisor API key, and reading local .env files can expose credentials.

Mitigation: Provide the key through a secure environment or secrets mechanism rather than searching .env files; do not include the key in responses.

Risk: The optional browser fallback uses a paired bridge tied to a TripAdvisor browser session.

Mitigation: Use the fallback only after reviewing the bridge's access and approving the pairing; prefer the API when a key is available.

## Reference(s):

- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Browser fallback guidance](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; browser fallback returns aggregate ratings but not individual review text.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
