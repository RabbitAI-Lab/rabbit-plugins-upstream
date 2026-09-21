## Description:

Query TripAdvisor location data from a shell with curl against the Terra REST API, with an optional fpx browser-bridge fallback for public location details when no API key is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor locations, nearby places, details, photos, and reviews through direct shell commands. It is useful when the TripAdvisor MCP server is unavailable or when a lightweight curl-based workflow is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to read TRIPADVISOR_API_KEY from a local .env file, which may expose secrets if commands or outputs are handled carelessly.

Mitigation: Provide the API key through a controlled secret mechanism, avoid printing it, and review generated shell commands before execution.

Risk: The optional fpx fallback can route requests through a signed-in browser session for tripadvisor.com.

Mitigation: Use fpx only when you understand that it relies on browser context, and pair it only for the intended TripAdvisor domain.

## Reference(s):

- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Web fallback via fpx](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API base URL](https://terra.tripadvisor.com/api)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, jq, and Python snippets; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor data workflows; requires TRIPADVISOR_API_KEY for Terra API calls and optional fpx setup for browser-mediated fallback details.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
