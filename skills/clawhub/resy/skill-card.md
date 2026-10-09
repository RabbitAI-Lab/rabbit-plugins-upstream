## Description:

Helps users search Resy restaurants and manage reservations, favorites, and Priority Notify subscriptions through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to find restaurant availability, book or cancel Resy reservations, and manage favorites and availability notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial MCP server receives the user's Resy email and password.

Mitigation: Use only if comfortable granting this access; keep credentials outside version-controlled files and restrict file permissions.

Risk: The server can book or cancel reservations and change favorites and notifications.

Mitigation: Review the venue, time, seating, fees, and cancellation terms in each booking or cancellation preview before confirming.

## Reference(s):

- [Resy skill listing](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Conversational text with reservation details, confirmation previews, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bookings and cancellations should be confirmed against the displayed details before proceeding.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
