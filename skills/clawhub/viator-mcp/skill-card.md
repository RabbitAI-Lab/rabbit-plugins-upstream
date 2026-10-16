## Description:

Search Viator tours, attractions, prices, and availability and share product links without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents can find tours and activities, compare product details and availability, and obtain links for completing purchases on Viator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup requires trusting an external package and providing a Viator Partner API key.

Mitigation: Review the package before installation and protect the key in MCP configuration.

Risk: Search and availability information does not complete a booking; availability prices may use supplier currency.

Mitigation: Check product links, current availability, and displayed currency before purchasing directly on Viator.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/viator-mcp)
- [Viator MCP package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns product details, prices, availability, and links for booking on Viator; does not book tours.]

## Skill Version(s):

2.1.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
