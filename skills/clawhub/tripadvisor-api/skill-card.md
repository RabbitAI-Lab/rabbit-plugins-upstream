## Description:

Query TripAdvisor location search, nearby results, details, photos, and reviews through the Terra REST API, with an optional browser based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill from a shell or script to retrieve TripAdvisor location information without installing the TripAdvisor MCP server. It supports location search, nearby results, details, photos, and reviews, with a browser based fallback for public location details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Terra API key could be exposed in logs or chat output.

Mitigation: Keep the key out of logs and chat; provide it through a protected environment variable.

Risk: API requests may consume paid quota.

Mitigation: Monitor usage and quota when making API requests.

Risk: The optional browser fallback connects a browser bridge to TripAdvisor fetches.

Mitigation: Verify the CLI and extension source, approve only TripAdvisor fetch access, and revoke the pairing when finished.

## Reference(s):

- [TripAdvisor Terra API endpoint examples](references/terra-endpoints.md)
- [Browser fallback guide](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API results and Markdown instructions with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested TripAdvisor location and available API access.]

## Skill Version(s):

1.1.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
