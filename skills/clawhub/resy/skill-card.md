## Description:

Helps agents search Resy restaurants and availability, manage reservations and favorites, and subscribe to Priority Notify through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy users can ask an agent to find restaurant availability, book or cancel tables, manage favorites, and set Priority Notify alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server accesses the user's Resy account using email and password through an unofficial private API.

Mitigation: Install only if comfortable with that access; keep the MCP configuration and credentials private.

Risk: Booking or cancelling a reservation can affect plans or incur fees.

Mitigation: Review the venue, time, seating and any fees in the preview before confirming.

## Reference(s):

- [Resy skill on ClawHub](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text and structured reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation are previewed for user confirmation.]

## Skill Version(s):

1.3.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
