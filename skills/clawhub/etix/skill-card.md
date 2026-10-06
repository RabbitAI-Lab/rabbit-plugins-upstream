## Description:

Search Etix events, venues, and performers and retrieve event and venue details through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find Etix events, performers, and venues and retrieve showtimes, locations, and available pricing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party package and browser extension route Etix requests through the user's open browser session.

Mitigation: Review the linked package and extension release before installation, and approve browser pairing intentionally.

Risk: This unofficial integration relies on Etix website endpoints that may change or fail.

Mitigation: Use it consistently with Etix's terms and verify event and price details on Etix before acting.

## Reference(s):

- [etix-mcp package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp project (linked in skill)](https://github.com/chrischall/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event and venue details may include dates, locations, and prices.]

## Skill Version(s):

1.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
