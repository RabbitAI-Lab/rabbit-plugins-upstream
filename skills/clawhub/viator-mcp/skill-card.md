## Description:

Helps agents search Viator tours and attractions and retrieve product details, availability, and pricing through a read-only MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and their users can find tours, activities, and attractions, then check product details, schedules, and prices. The connector supports discovery, not booking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party connector requires trusting its package or source.

Mitigation: Verify the third-party package or source before installation.

Risk: The connector needs a Viator Partner API key that may remain in the MCP configuration.

Mitigation: Use a key intended for this connector and remove the MCP entry and key setting when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/viator-mcp)
- [viator-mcp npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text with tour and attraction details, availability, pricing, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability prices may be in the supplier's currency; no bookings are performed.]

## Skill Version(s):

2.1.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
