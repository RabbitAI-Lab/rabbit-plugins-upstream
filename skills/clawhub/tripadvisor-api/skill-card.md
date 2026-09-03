## Description:

Query TripAdvisor location data from a shell with curl against the Terra REST API, with a browser-bridge fallback for public location details when no API key is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor search, nearby, detail, photo, and review data through read-only Terra API calls, or to extract limited public location details through a browser-mediated fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TripAdvisor API keys may be exposed if pasted into shell history, logs, or shared transcripts.

Mitigation: Keep the key in a private environment variable, avoid echoing it, and rotate it if it may have been disclosed.

Risk: The optional fpx fallback fetches TripAdvisor pages through a paired browser session.

Mitigation: Pair only with a browser profile you trust, use the fallback only when needed, and remove the fpx profile after use if it is no longer required.

Risk: The browser fallback can return incomplete or stale location details if TripAdvisor page markup changes or a bot challenge is returned.

Mitigation: Prefer Terra API endpoints for structured data and re-check fallback results before using them in user-facing decisions.

## Reference(s):

- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [TripAdvisor Developers](https://www.tripadvisor.com/developers)
- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, API calls]

**Output Format:** [Markdown guidance with curl, jq, shell, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only request recipes and parsing guidance; API responses are JSON when returned by Terra.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
