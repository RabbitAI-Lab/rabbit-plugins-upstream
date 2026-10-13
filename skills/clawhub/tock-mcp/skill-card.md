## Description:

Helps agents discover Tock restaurants, check experiences and availability, and inspect a signed-in user's reservations through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for Tock restaurants can compare venues, experiences, prices, party sizes, and available times. Signed-in users can inspect their reservations and verify a booking made on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP server and browser extension can access pages in a Tock tab.

Mitigation: Verify the npm package and ContextMint Bridge release or source before installing.

Risk: Signed-in account tools can read Tock profile and reservation details.

Mitigation: Use signed-in mode only if you are comfortable sharing those details with the MCP flow; complete bookings and payments on Tock.

Risk: A booking success screen or an immediate missing reservation can misstate booking status.

Mitigation: Require a receipt or confirmation ID and a confirmed reservation-check verdict; recheck when results are inconclusive.

## Reference(s):

- [ClawHub tock-mcp release](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with structured venue, availability, and reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking confirmation requires a receipt or confirmation ID and a confirmed reservation-check verdict.]

## Skill Version(s):

1.1.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
