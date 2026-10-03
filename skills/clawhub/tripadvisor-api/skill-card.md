## Description:

Guides agents to retrieve TripAdvisor location search results, details, photos, and reviews through the Terra API, with a browser-based fallback for public location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up TripAdvisor locations, nearby places, photos, and reviews without an MCP server. A paired browser can retrieve limited public location details when an API key is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A TripAdvisor API key may be exposed when copied or printed from a local .env file.

Mitigation: Provide TRIPADVISOR_API_KEY through normal secret management and avoid printing it in terminal output.

Risk: The optional browser fallback requires pairing a browser bridge and saving fetched page HTML locally.

Mitigation: Use the fallback only if comfortable pairing the bridge for tripadvisor.com and writing fetched HTML to /tmp.

## Reference(s):

- [ClawHub tripadvisor-api release](https://clawhub.ai/chrischall/skills/tripadvisor-api)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)
- [Terra endpoint recipes](references/terra-endpoints.md)
- [Browser fallback guide](references/web-fallback.md)
- [ContextMint Bridge source and releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API lookups return read-only location data; browser fallback provides limited public location details.]

## Skill Version(s):

1.1.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
