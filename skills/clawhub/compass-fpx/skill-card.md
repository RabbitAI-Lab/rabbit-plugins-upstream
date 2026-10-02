## Description:

Helps agents query Compass real-estate listings, property and agent details, price history, and street addresses from a shell through a paired browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US real-estate listings, resolve addresses, and retrieve Compass property, agent, and price-history details without an MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing the browser bridge can expose the active Compass session to skill-driven requests.

Mitigation: Use a dedicated browser profile when session separation matters and scope extension site access to compass.com.

Risk: Searched addresses are sent to Compass.

Mitigation: Avoid entering sensitive addresses unless sharing them with Compass is appropriate.

Risk: Example commands can overwrite existing files in /tmp.

Mitigation: Choose unique output paths before running the examples.

## Reference(s):

- [Compass FPX on ClawHub](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request recipes](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can extract listing, property, and agent data as JSON; access depends on a paired Compass browser tab.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
