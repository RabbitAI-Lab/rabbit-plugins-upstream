## Description:

Helps agents search Viator tours and attractions, inspect product details and availability, and compare prices without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and other users can find tours, activities, attractions, and availability by destination, then follow product links to book on Viator. Developers can configure the required Viator Partner API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party package and exposing a Viator Partner API key can compromise credentials if the setup is not trusted.

Mitigation: Install only when the package is intended for use, prefer project-level configuration, and treat VIATOR_API_KEY as a secret.

Risk: Availability and prices may change or appear in the supplier's currency rather than the requested currency.

Mitigation: Check availability and currency before sharing prices, convert supplier-currency amounts where needed, and confirm details on Viator before booking.

## Reference(s):

- [ClawHub viator-mcp release](https://clawhub.ai/chrischall/skills/viator-mcp)
- [viator-mcp npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown responses with product links; JSON for setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only search and lookup; booking occurs on Viator.]

## Skill Version(s):

2.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
