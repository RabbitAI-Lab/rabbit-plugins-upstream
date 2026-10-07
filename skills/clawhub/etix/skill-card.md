## Description:

Search Etix events, venues, and performers and retrieve event and venue details through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents help users discover Etix events, performers, and venues and retrieve show details, including dates, locations, and available pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial integration routes automated requests through an active Etix browser session and may affect the session or conflict with service terms.

Mitigation: Review Etix terms before use, limit bridge access to Etix, and use a project-scoped MCP configuration.

Risk: Installing the MCP package and third-party browser extension introduces external software into the browsing workflow.

Mitigation: Review or pin the npm package and extension release before installing.

## Reference(s):

- [Etix skill on ClawHub](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event and venue details may include dates, addresses, and prices.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
