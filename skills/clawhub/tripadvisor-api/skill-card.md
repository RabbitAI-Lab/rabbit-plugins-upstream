## Description:

Helps agents retrieve TripAdvisor location search results, details, photos, and reviews through the read-only Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor places, photos, and reviews from a shell without running an MCP server. With a known location ID, they can retrieve limited public details through their signed-in browser when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A TripAdvisor API key may be exposed while following shell setup steps.

Mitigation: Provide TRIPADVISOR_API_KEY securely and avoid printing or sharing its value.

Risk: Browser fallback requests use the user's signed-in TripAdvisor browser context.

Mitigation: Use the fallback only when comfortable routing requests through that signed-in browser session.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Terra endpoint recipes](references/terra-endpoints.md)
- [Browser fallback instructions](references/web-fallback.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only location data; browser fallback returns aggregate ratings but not individual review text.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
