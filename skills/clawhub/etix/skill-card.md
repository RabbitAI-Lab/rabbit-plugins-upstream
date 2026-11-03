## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to discover Etix events, venues, and performers, then retrieve event or venue details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use the user's Etix browser session through the ContextMint Bridge extension.

Mitigation: Pin a reviewed etix-mcp version, verify the extension download using its published checksum, and review the domains and permissions before approving pairing.

Risk: The integration is unofficial and relies on Etix website endpoints that may change.

Mitigation: Use it for event discovery at your discretion and recheck the integration if Etix changes its site behavior or terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [Project source linked in the skill documentation](https://github.com/chrischall/etix-mcp)
- [npm package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Etix ticket site](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Event and venue search results and details, summarized in natural language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, the ContextMint Bridge extension, and an open Etix tab with pairing approved.]

## Skill Version(s):

1.1.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
