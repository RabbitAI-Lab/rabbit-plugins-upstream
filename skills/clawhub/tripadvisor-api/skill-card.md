## Description:

Query TripAdvisor location data for search, nearby places, details, photos, and reviews from a shell with curl against the Terra REST API, with a no-API-key fallback for public location details through the fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data without running the TripAdvisor MCP server, especially for shell scripts or environments where MCP tooling is not installed. It supports Terra API calls with a TripAdvisor API key and a narrower browser-mediated fallback for public location details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a TripAdvisor API key in curl headers, and careless shell history or environment handling can expose that credential.

Mitigation: Set TRIPADVISOR_API_KEY explicitly in the environment, avoid copying secrets into shared files or logs, and prefer a dedicated key with the minimum needed access.

Risk: The optional fpx fallback routes public TripAdvisor page fetches through a paired browser tab, which can inherit browser session state.

Mitigation: Use a dedicated or logged-out browser profile for the fpx fallback when possible and pair only the TripAdvisor fetch capability needed for the task.

Risk: TripAdvisor API quota limits or invalid key families can interrupt requests and produce 401, 403, or 429 responses.

Mitigation: Check API family and quota before relying on the skill in automation, and add backoff or retry handling for quota responses.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, curl examples, jq projections, and JSON response notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor data retrieval guidance; responses from the Terra API are JSON and should be inspected or transformed with jq.]

## Skill Version(s):

0.5.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
