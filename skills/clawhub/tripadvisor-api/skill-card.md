## Description:

Query TripAdvisor location data for search, nearby places, details, photos, and reviews from a shell with curl against the Terra REST API, with a no-API-key fallback for public location details through fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data from Terra API endpoints without running the TripAdvisor MCP server. It is useful for shell-based lookups, scripts, and environments where MCP installation is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a TripAdvisor API key and includes a command that may expose environment-file contents in an agent transcript or shared terminal.

Mitigation: Set TRIPADVISOR_API_KEY through a secure environment or secret manager, and avoid printing .env contents in shared contexts.

Risk: The fallback uses fpx with a signed-in browser session to fetch TripAdvisor pages.

Mitigation: Pin and review the fpx CLI version, understand the browser-session access it uses, and limit fallback use to contexts where that access is appropriate.

Risk: The fallback writes fetched TripAdvisor HTML to a fixed /tmp path before parsing.

Mitigation: Use a secure temporary file path and delete the fetched HTML after parsing.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown guidance with curl, jq, and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only API lookup guidance and shell recipes; no TripAdvisor write operations are described.]

## Skill Version(s):

0.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
