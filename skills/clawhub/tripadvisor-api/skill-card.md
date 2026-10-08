## Description:

Guides agents in retrieving TripAdvisor location search results, nearby places, details, photos, and reviews through the Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor places and retrieve location details, photos, and reviews from a shell without running an MCP server. A signed-in browser can provide basic public location details when no API key is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key may be exposed when copied from local files or printed in command output.

Mitigation: Use a preconfigured environment variable or secret manager; do not grep or print real API keys.

Risk: The browser fallback uses a paired extension with access to a signed-in TripAdvisor session.

Mitigation: Enable the fallback only if you trust the extension and use a dedicated browser profile.

## Reference(s):

- [Terra API endpoint recipes](references/terra-endpoints.md)
- [Browser fallback instructions](references/web-fallback.md)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Code]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location lookups; the browser fallback returns aggregate ratings but not individual review text.]

## Skill Version(s):

1.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
