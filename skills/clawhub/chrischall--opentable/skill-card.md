## Description:

Helps agents search OpenTable restaurants and availability, book or manage reservations, and manage favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners and their agents can find restaurants and available tables, book or change reservations, review upcoming bookings, and manage saved restaurants using an authenticated OpenTable session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses the user's signed-in OpenTable browser session.

Mitigation: Install only if comfortable granting this access; remove the MCP entry or browser extension when it is no longer needed.

Risk: Bookings or changes may involve card holds or cancellation charges.

Mitigation: Review booking previews, cancellation policies, and card-hold details before approving a reservation or change.

## Reference(s):

- [OpenTable skill release](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include restaurant options, available slots, reservation details, and confirmation information.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
