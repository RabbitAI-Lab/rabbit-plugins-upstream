## Description:

Helps agents discover Tock restaurants, check bookable experiences and availability, and inspect a signed-in user's reservations and profile through a read-only MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners and agents use this skill to find Tock venues and experiences, inspect available dates and times, and check their own reservation details. Booking and payment remain on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension can expose signed-in Tock profile, email, and reservation history to the agent.

Mitigation: Install only if comfortable with the integration; use account tools only when intending to share that data, and remove the MCP configuration or bridge pairing when access is no longer wanted.

## Reference(s):

- [tock-mcp on ClawHub](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with reservation and venue details, plus setup examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock queries; account data requires a signed-in browser session.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
