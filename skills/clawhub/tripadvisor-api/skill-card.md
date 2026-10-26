## Description:

Guides agents to retrieve TripAdvisor location data through the Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can search for TripAdvisor places and retrieve nearby locations, details, photos, and reviews using shell-based Terra API requests. A browser fallback can retrieve public location details when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading a local .env file to recover an API key can expose credentials to the agent.

Mitigation: Provide TRIPADVISOR_API_KEY through a secure environment or secret manager instead of letting the agent read .env files.

Risk: The optional browser fallback fetches pages through a signed-in TripAdvisor browser context.

Mitigation: Prefer the Terra API; if using the fallback, pair a dedicated low-privilege browser profile and verify the CLI and extension source.

## Reference(s):

- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Browser fallback guide](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell examples and JSON location data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; the browser fallback returns location details and aggregate ratings, not individual review text.]

## Skill Version(s):

1.1.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
