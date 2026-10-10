## Description:

Helps agents query TripAdvisor locations, photos, and reviews through the read-only Terra API, with a browser-assisted fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor locations, nearby places, details, photos, and reviews without running an MCP server. Public location details can also be retrieved through a paired browser when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key may be exposed if printed from a local environment file or included in shared command output.

Mitigation: Set TRIPADVISOR_API_KEY using a secret manager or shell environment, and avoid printing or sharing the key.

Risk: Pairing the browser fetch bridge grants access to requests through the signed-in TripAdvisor tab.

Mitigation: Approve pairing only for the intended TripAdvisor profile and use the bridge only when needed.

## Reference(s):

- [TripAdvisor API skill release](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Terra endpoint recipes](artifact/references/terra-endpoints.md)
- [Browser fallback guide](artifact/references/web-fallback.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell examples and JSON location data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location data; review text requires the API rather than the browser fallback.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
