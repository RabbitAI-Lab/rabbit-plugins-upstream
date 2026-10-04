## Description:

Helps agents find Etix events, performers, and venues and retrieve event and venue details through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents searching Etix can find events, performers, and venues, then retrieve event dates, locations, and pricing information. The integration requires an MCP server, a browser extension, and an open Etix tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the MCP package and browser extension adds third-party software to the user's environment.

Mitigation: Verify the npm package and ContextMint Bridge release or source before installation.

Risk: Requests use the user's open Etix browser tab and session, and the site has no public consumer API.

Mitigation: Only pair the bridge when comfortable with browser-session access and Etix terms-of-use risk; review retrieved details before relying on them.

## Reference(s):

- [ClawHub etix skill listing](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language event and venue details with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include event and venue IDs and Etix URLs; event details may include dates, locations, and prices.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
