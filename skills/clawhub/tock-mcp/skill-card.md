## Description:

Helps agents discover Tock restaurants, check experiences and availability, and look up reservations through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving diners can find Tock restaurants, view bookable experiences and availability, and check a signed-in user's reservations. Booking and payment take place on Tock, not through this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account tools access a signed-in Tock session and can expose profile and reservation information.

Mitigation: Trust the Tock MCP package and ContextMint Bridge extension before installing, and limit account lookups to the intended user's session.

Risk: A booking success screen or an immediate missing reservation may not reliably establish booking status.

Mitigation: Require a receipt or confirmation identifier and a confirmed reservation check; otherwise report the attempt as unverified and recheck after a delay.

## Reference(s):

- [Tock MCP on ClawHub](https://clawhub.ai/chrischall/skills/tock-mcp)
- [Tock MCP npm package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown responses based on MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Restaurant, availability, profile, and reservation information; account lookups require a signed-in Tock tab. No booking, cancellation, or payment actions.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
