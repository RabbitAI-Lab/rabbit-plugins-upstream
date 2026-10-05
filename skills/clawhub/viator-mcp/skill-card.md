## Description:

Helps agents search Viator tours, attractions, pricing, and availability without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and their agents use this skill to find Viator experiences, compare product details and availability, browse attractions, and check prices. Bookings take place through Viator product links outside the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted connector package or exposing a Viator API key.

Mitigation: Confirm you trust the referenced package before installation and use a Viator Partner API key intended for this connector.

Risk: Treating search results as confirmed bookings or supplier-currency prices as converted prices.

Mitigation: Book only through Viator product URLs and clearly label prices; convert supplier-currency availability quotes when needed.

## Reference(s):

- [ClawHub viator-mcp release](https://clawhub.ai/chrischall/skills/viator-mcp)
- [viator-mcp npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tour and attraction details may include prices, availability, and product URLs; booking is not supported.]

## Skill Version(s):

2.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
