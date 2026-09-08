## Description:

Query TripAdvisor location data for search, nearby places, details, photos, and reviews from a shell using curl against the Terra REST API, with an fpx browser-bridge fallback for public location details when no API key is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce curl and jq workflows for retrieving TripAdvisor location data without running an MCP server. It also guides key-free public detail lookup through fpx when Terra API access is unavailable or blocked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can expose a local TripAdvisor API key if users print or paste environment-file contents.

Mitigation: Provide TRIPADVISOR_API_KEY through a secure environment variable or secret manager and avoid commands that print secrets.

Risk: The fpx fallback depends on a globally installed, unpinned CLI and the Transporter browser extension.

Mitigation: Use the fallback only after reviewing and trusting those components; prefer a pinned or locally managed installation over installing the latest global package.

Risk: The browser-bridge fallback requires an active signed-in TripAdvisor browser context and may fail behind bot-wall or extension-connection states.

Mitigation: Use a dedicated trusted browser profile, keep the TripAdvisor tab scoped to the intended fetch, and retry only after confirming the expected extension and page state.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback: location detail via fpx](references/web-fallback.md)
- [TripAdvisor Developers](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, curl, jq, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs read-only TripAdvisor API and browser-bridge retrieval instructions; Terra API responses are JSON.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
