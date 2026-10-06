## Description:

Helps users find restaurants and available tables, book or manage OpenTable reservations, and manage favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners use this skill to search restaurant availability, make or change reservations, review upcoming bookings, cancel reservations, and save favorite restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server and browser extension can act through the user's signed-in OpenTable session.

Mitigation: Review the package and extension before installation, and use only with a session you are comfortable granting them access to.

Risk: Booking, changing, or cancelling a reservation can have financial or scheduling consequences, including card holds or no-show fees.

Mitigation: Confirm the reservation details, cancellation policy, and any card-hold or no-show terms with the user before committing changes.

## Reference(s):

- [OpenTable skill on ClawHub](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge installation](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with reservation and availability details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the MCP server and browser extension with an active OpenTable sign-in.]

## Skill Version(s):

1.2.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
