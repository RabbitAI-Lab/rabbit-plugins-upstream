## Description:

Helps agents search Viator tours and activities, compare product details and pricing, and check availability without making bookings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and agents use this skill to find Viator experiences, compare product details and prices, and check availability before directing travelers to Viator to book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party connector requires trusting its package or source.

Mitigation: Verify the publisher and review the package or source before installing.

Risk: The Viator Partner API key is placed in MCP environment configuration.

Mitigation: Keep the key in a protected configuration and do not commit it to a repository.

Risk: Availability prices use the supplier's currency and may differ from search prices.

Mitigation: Check currencies and current availability before quoting a price or sending a traveler to Viator to book.

## Reference(s):

- [Viator MCP on ClawHub](https://clawhub.ai/chrischall/skills/viator-mcp)
- [Viator MCP npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tour recommendations, product details, prices, availability and links to book on Viator.]

## Skill Version(s):

2.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
