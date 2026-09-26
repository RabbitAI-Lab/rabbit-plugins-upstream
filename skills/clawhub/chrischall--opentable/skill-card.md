## Description:

Helps users find restaurants and availability, manage OpenTable reservations, and save favorite restaurants through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to plan dining can search restaurants, check open tables, book or change reservations, review upcoming bookings, cancel bookings, and manage favorites on OpenTable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension can act through a signed-in OpenTable session, and the external software is outside the scanned skill artifact.

Mitigation: Install only if comfortable granting that access; review the external package and extension before use.

Risk: Booking, changing, or canceling a reservation can involve a saved card, no-show fees, or cancellation charges.

Mitigation: Review the action preview, payment details, and cancellation policy, and approve the exact action before it proceeds.

## Reference(s):

- [OpenTable skill release on ClawHub](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp documentation](https://github.com/chrischall/opentable-mcp)
- [fetchproxy browser extension documentation](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with restaurant options, availability, reservation details, and action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed MCP server and browser extension with a signed-in OpenTable tab; booking, modification, and cancellation require confirmation.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
