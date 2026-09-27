## Description:

Helps agents retrieve TripAdvisor location searches, nearby places, details, photos, and reviews through read-only API calls, with a browser-based fallback for basic location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor places, ratings, photos, and reviews without an MCP server. A browser-session fallback provides basic location details when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading or printing a .env file may expose the TripAdvisor API key.

Mitigation: Provide the key through a secret manager or environment variable instead of printing it from a .env file.

Risk: The fallback accesses a signed-in browser session and can leave fetched page content in a temporary file.

Mitigation: Limit browser access to tripadvisor.com and delete /tmp/ta-location.html if it may contain session-contextualized content.

## Reference(s):

- [TripAdvisor API skill on ClawHub](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Terra API endpoint recipes](artifact/references/terra-endpoints.md)
- [Browser fallback instructions](artifact/references/web-fallback.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and shell commands with JSON location data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location data; browser fallback returns basic details, not individual review text.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
