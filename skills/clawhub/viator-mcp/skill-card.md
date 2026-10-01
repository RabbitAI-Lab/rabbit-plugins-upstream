## Description:

Helps agents search Viator tours and attractions and check product details, prices, and availability without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and their agents use this skill to find Viator activities, compare details and availability, and obtain links for booking externally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the referenced npm package and storing a Viator Partner API key in MCP configuration.

Mitigation: Install only if you trust the package and protect the API key in your MCP configuration.

Risk: Search queries are sent to Viator and bookings occur through external Viator links.

Mitigation: Avoid including sensitive details in searches and review the destination link before booking.

## Reference(s):

- [ClawHub release](https://clawhub.ai/chrischall/skills/viator-mcp)
- [viator-mcp npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tour and attraction details, prices, availability, and external booking links; no in-skill booking.]

## Skill Version(s):

2.1.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
