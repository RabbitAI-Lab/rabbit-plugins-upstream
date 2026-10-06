## Description:

Helps agents find Tock restaurants, experiences, prices, and availability, and check a signed-in user's reservations through a read-only MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching Tock restaurants use this skill to compare venues and available experiences; signed-in users can inspect their profile and reservations and verify a booking made on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and browser extension access Tock through the user's browser; account tools can read profile and reservation details.

Mitigation: Install the package and extension only if you trust them, and use signed-in account tools only when you want the agent to see those details.

Risk: A booking success screen or immediate absence from reservation history may misstate whether a reservation was confirmed.

Mitigation: Complete booking and payment on Tock, then require a receipt or confirmation ID plus a confirmed verification result; recheck after a delay if advised.

## Reference(s):

- [Tock MCP on ClawHub](https://clawhub.ai/chrischall/skills/tock-mcp)
- [Tock MCP npm package](https://www.npmjs.com/package/tock-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured MCP results and natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; account tools require a signed-in Tock tab.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
