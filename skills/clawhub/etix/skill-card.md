## Description:

Helps agents search Etix events, venues, and performers and retrieve event and venue details through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for Etix shows can search by event, venue, performer, or location and retrieve event schedules, venue details, and available price information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookups pass through an open Etix browser tab using its cookies and session.

Mitigation: Use a browser session you are comfortable sharing with the integration, and review the bridge extension and etix-mcp package before installing.

Risk: The integration relies on Etix website endpoints, which may change or become unavailable.

Mitigation: Check results against Etix before relying on event details or prices, and use the health check when lookups fail.

## Reference(s):

- [Etix skill listing](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include Etix URLs and IDs; event and venue details may include showtimes, locations, and prices.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
