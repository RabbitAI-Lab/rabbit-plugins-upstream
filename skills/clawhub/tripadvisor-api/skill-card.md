## Description:

Query TripAdvisor location data for search, nearby places, details, photos, and reviews from a shell with curl against the Terra REST API, with a no-API-key fallback that reads a public location page through the fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data through shell commands for scripts or environments where the MCP server is unavailable. It supports API-key based Terra reads and a smaller browser-bridge fallback for public location details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TripAdvisor API keys may be exposed through shell commands, environment handling, or local .env inspection.

Mitigation: Set TRIPADVISOR_API_KEY through a normal secret manager or scoped environment and avoid printing or copying secrets into shared logs.

Risk: The fpx fallback uses a signed-in browser bridge and may expose browsing context or temporary fetched HTML.

Mitigation: Use a dedicated browser profile restricted to tripadvisor.com, delete temporary fetched HTML, and unpair or remove fpx when the fallback is no longer needed.

Risk: API quotas, upstream errors, bot walls, or page parsing drift may produce missing or incomplete results.

Mitigation: Check HTTP status and error bodies, back off on 429 responses, and verify parsed fallback results before relying on them.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback: location detail via fpx](references/web-fallback.md)
- [TripAdvisor Developers](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, jq, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only TripAdvisor API and browser-fallback guidance; command results are expected to be JSON or parsed JSON projections.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
