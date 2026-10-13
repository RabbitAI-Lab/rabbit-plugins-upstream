## Description:

Helps agents search Viator tours and attractions, check product details and availability, and convert supplier-currency prices without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and their users can discover Viator experiences, compare details and prices, and check availability before visiting Viator to book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party MCP package and a Viator Partner API key.

Mitigation: Verify that you trust the package before installation and use a key you are comfortable placing in MCP environment configuration.

Risk: Tour details and prices are retrieved from Viator, and bookings are not performed by this skill.

Mitigation: Confirm current availability and pricing with Viator before booking through the provided product link.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/viator-mcp)
- [viator-mcp npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and availability information may include prices and booking links; the skill does not make bookings.]

## Skill Version(s):

2.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
