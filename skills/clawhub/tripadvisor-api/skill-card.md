## Description:

Query TripAdvisor location data for search, nearby places, details, photos, and reviews from shell commands against the Terra REST API, with a browser-session fallback for public location details when an API key is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data through reproducible curl, jq, and fpx workflows without running the TripAdvisor MCP server. It supports scripted lookups for search, nearby results, details, photos, reviews, and limited no-key public-page detail extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional fpx fallback routes requests through a signed-in TripAdvisor browser context.

Mitigation: Use the Terra API-key workflow when possible, and pair only a browser profile intentionally authorized for this read-only lookup.

Risk: TripAdvisor public-page parsing can fail or return limited data when the page shape changes or a bot-challenge page is returned.

Mitigation: Treat the fallback as limited to public core details, refresh or re-authorize the browser tab when needed, and use Terra endpoints for search and review text.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor developers](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, jq, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TripAdvisor API and public-page lookup guidance; Terra responses are JSON and the fpx fallback parses public HTML into JSON.]

## Skill Version(s):

0.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
