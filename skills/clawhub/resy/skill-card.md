## Description:

Helps agents search Resy venues, manage reservations and favorites, and subscribe to Priority Notify through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can find available tables, book or cancel reservations, manage favorite venues, and subscribe to Priority Notify on their Resy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to the Resy account session and locally cached authentication token can expose account information.

Mitigation: Install only if comfortable granting account access; review token-cache settings and protect the account session.

Risk: Booking or cancelling a reservation may involve fees or unintended account changes.

Mitigation: Review the venue, time, party size, and fees in the confirmation preview before approving a booking or cancellation.

Risk: The server uses Resy's private web API, whose behavior may change.

Mitigation: Review the private-API warning and verify reservation status before retrying an uncertain booking or cancellation.

## Reference(s):

- [Resy skill on ClawHub](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp package](https://www.npmjs.com/package/resy-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes availability, reservation details, and confirmation previews.]

## Skill Version(s):

1.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
