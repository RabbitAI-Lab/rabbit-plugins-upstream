## Description:

Provides shell-oriented guidance for querying TripAdvisor location search, nearby results, details, photos, and reviews through the Terra REST API, with a browser-bridge fallback for key-free public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve TripAdvisor location data from shell workflows without running the MCP server. It helps construct curl, jq, and fallback browser-bridge commands for read-only TripAdvisor lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can expose or mishandle TRIPADVISOR_API_KEY if copied directly into shared shells, logs, or command history.

Mitigation: Provide the API key through the user's normal secret-management flow and avoid printing or committing it.

Risk: The fallback browser bridge can access an authenticated TripAdvisor browser session.

Mitigation: Use a dedicated browser profile or account for fpx and approve only the fetch capability needed for TripAdvisor pages.

Risk: The fallback setup suggests a global npm install without pinning the package version.

Mitigation: Prefer a reviewed, pinned, or locally managed @fetchproxy/cli installation where possible.

## Reference(s):

- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Web fallback details](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, curl examples, jq filters, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only TripAdvisor lookup guidance; generated commands may require a TripAdvisor Terra API key or a paired browser bridge.]

## Skill Version(s):

0.6.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
