## Description:

Search Viator tours, activities, experiences, attractions, availability, pricing, and destination data through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Viator travel products, compare details, pricing, availability, destinations, and attractions, and route users to Viator product URLs for booking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Viator Partner API key and sends travel search queries through the referenced npm package.

Mitigation: Use a dedicated Viator Partner API key, scope its use to intended agents, and pin or review the package/source before using npx.

Risk: The skill is read-only and cannot complete bookings.

Mitigation: Treat returned product and attraction URLs as handoff links for booking on Viator, and do not represent search output as a completed reservation.

Risk: Availability schedules and supplier-currency pricing can differ from search result currency.

Mitigation: Check availability details before presenting final options and convert supplier-currency prices when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package: @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Skill-declared source repository](https://github.com/chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text travel search results with MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only travel search; booking is handled through returned Viator URLs.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
