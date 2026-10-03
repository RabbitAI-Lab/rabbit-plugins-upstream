## Description:

Helps agents find Tock restaurants, experiences, and availability, and read or verify reservations through the user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents planning restaurant visits use this skill to discover Tock venues, compare experiences and open times, and check their own reservations. Booking and payment take place on Tock, not through this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension access Tock through the user's browser session.

Mitigation: Verify that both components are trusted before installation and approve browser pairing deliberately.

Risk: Account tools can read personal profile and reservation information.

Mitigation: Use account tools only when needed and avoid sharing their responses beyond the intended user.

Risk: A booking success screen or an immediate missing reservation can misrepresent booking status.

Mitigation: Treat booking as unverified until a receipt or confirmation ID and a confirmed reservation check agree; recheck after a short delay if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured MCP tool results and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery and account lookups; account tools require a signed-in Tock browser tab.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
