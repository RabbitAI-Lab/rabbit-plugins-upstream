## Description:

Query TripAdvisor location search, nearby places, details, photos, and reviews from the Terra REST API with curl, with an optional fpx browser-bridge fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate read-only TripAdvisor lookup workflows for location search, nearby discovery, details, photos, and reviews. It is useful when the TripAdvisor MCP server is not installed or when a direct shell-based API call is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can expose a TripAdvisor API key if a user runs a command that prints TRIPADVISOR_API_KEY from a local .env file.

Mitigation: Set the key through a normal secret manager or environment without printing its value, and do not run commands that display the secret.

Risk: The optional fpx fallback installs an unpinned global browser-bridge CLI.

Mitigation: Treat the fallback as optional, review the @fetchproxy/cli package before installation, avoid elevated privileges, and pin or approve the dependency through local policy.

Risk: The fallback recipe writes fetched TripAdvisor HTML to a fixed /tmp path.

Mitigation: Replace the fixed /tmp output path with a mktemp-created file before using the fallback in shared or automated environments.

## Reference(s):

- [Terra API endpoints](references/terra-endpoints.md)
- [Web fallback](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only API-call recipes; commands may require TRIPADVISOR_API_KEY or optional fpx setup.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
