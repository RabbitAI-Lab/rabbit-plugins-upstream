## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, cancellation, favorites, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Resy reservation workflows such as searching availability, booking tables, cancelling reservations, managing favorites, and subscribing to Priority Notify. It is intended for users who have a Resy account and are comfortable configuring account credentials for the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires access to a user's Resy account credentials.

Mitigation: Use local secret storage where possible and keep RESY_EMAIL and RESY_PASSWORD out of source control and shared configuration files.

Risk: Booking or cancellation tools can change a user's real restaurant reservations.

Mitigation: Review venue, date, time, party size, fees, and cancellation details before confirming an action or supplying a confirmToken.

Risk: The integration depends on private Resy web-app behavior rather than an official public API.

Mitigation: Use the skill only if you accept that endpoint behavior may change and validate important reservation actions in Resy when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration examples, shell commands, and MCP tool result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation actions require explicit user confirmation or a confirmToken before completion.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
