## Description:

Provides shell-oriented guidance for querying TripAdvisor Terra location APIs with curl and jq, plus a browser-bridge fallback for public location details when no API key is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location search, nearby, details, photos, and reviews data from the Terra API without running the MCP server. It also supports limited public-page detail extraction through a signed-in browser bridge when a Terra API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to expose a TripAdvisor API key from a local .env file.

Mitigation: Provide TRIPADVISOR_API_KEY explicitly without grepping or printing .env files, and avoid logging secrets in shell history or command output.

Risk: The fallback path installs and pairs an unpinned browser bridge.

Mitigation: Pin and review the fpx installation, use a dedicated low-privilege browser profile, and revoke the pairing after use.

Risk: The fallback recipe writes to a fixed /tmp filename.

Mitigation: Use a unique temporary file path with restricted permissions for fetched TripAdvisor HTML.

## Reference(s):

- [TripAdvisor Developer Portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)
- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, jq, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only API recipes and fallback parsing guidance; Terra responses are JSON.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
