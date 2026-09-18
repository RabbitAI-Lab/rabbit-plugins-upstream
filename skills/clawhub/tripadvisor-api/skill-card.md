## Description:

Guides agents to query TripAdvisor Terra location data with curl for search, nearby places, details, photos, and reviews, with an optional fpx browser-bridge fallback for public page details when no API key is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data directly from the Terra REST API without running the TripAdvisor MCP server. It also provides a limited no-key fallback for reading public location details through a paired browser bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can expose a local TripAdvisor API key when reading from a .env file.

Mitigation: Provide TRIPADVISOR_API_KEY through a secure environment variable or secret manager, and avoid printing or copying secrets from local files.

Risk: The fallback flow asks the user to install and pair a global browser-bridge CLI.

Mitigation: Prefer a pinned or local install for @fetchproxy/cli, pair only the required TripAdvisor profile, and revoke the browser pairing when finished.

Risk: The fallback example writes fetched HTML to a fixed /tmp filename.

Mitigation: Use a securely generated temporary file for fetched pages and delete it after parsing.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor data retrieval; API-key calls require TRIPADVISOR_API_KEY and fallback details require fpx with a paired browser tab.]

## Skill Version(s):

0.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
