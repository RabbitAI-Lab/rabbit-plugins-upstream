## Description:

Helps agents retrieve TripAdvisor location search results, details, photos, and reviews through the Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor places, ratings, photos, and reviews without running an MCP server. A browser fallback can retrieve public details for a known location when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading a local .env file may expose a TripAdvisor API key.

Mitigation: Provide the key explicitly through an approved secret mechanism rather than reading local credential files.

Risk: Installing a global browser bridge and pairing a signed-in tab can expose browser-session data.

Mitigation: Prefer the read-only Terra API; review the bridge before installation and pair only an approved browser tab if the fallback is needed.

Risk: The browser fallback can leave fetched page HTML in a temporary file.

Mitigation: Delete temporary HTML after extracting the needed location details.

## Reference(s):

- [TripAdvisor API skill listing](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [Terra endpoint recipes](references/terra-endpoints.md)
- [Browser fallback instructions](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location data; the browser fallback provides summary details, not individual review text.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
