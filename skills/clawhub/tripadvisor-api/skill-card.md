## Description:

Helps agents query TripAdvisor location data from a shell with curl against the Terra REST API, with a browser-bridge fallback for reading public location detail pages when an API key is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to retrieve TripAdvisor search, nearby, details, photos, and reviews data in scripts or agent workflows without relying on the TripAdvisor MCP server. It also supports reading limited public page details through a browser bridge when a Terra API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TripAdvisor API keys could be exposed through shell history, logs, or overly broad credential use.

Mitigation: Use a least-privilege API key, store it in an environment variable, and avoid echoing or logging commands that reveal the key.

Risk: The browser-bridge fallback can involve an existing signed-in TripAdvisor browser session.

Mitigation: Confirm the global fpx install and Transporter pairing are acceptable, and use a dedicated browser profile when normal session context should stay separate.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [TripAdvisor Developers](https://www.tripadvisor.com/developers)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only TripAdvisor API and browser-fetch workflows; API responses are expected to be JSON for jq processing.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
