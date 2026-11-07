## Description:

Manage OpenTable restaurant menus, availability, reservations, and favorites through an MCP server connected to a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can find restaurants, compare published menus and available times, manage favorites, and manage OpenTable reservations through natural-language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a separately installed MCP package and browser extension.

Mitigation: Trust and pin the npm package and browser-extension versions before installing.

Risk: Booking, modification, or cancellation can create reservation commitments and may involve card holds or cancellation fees.

Mitigation: Keep reservation confirmations enabled and review the action preview, payment details, and cancellation policy before approving.

Risk: Reservation security tokens can authorize cancellation, and access uses the signed-in OpenTable browser session.

Mitigation: Protect reservation security tokens and use a trusted, signed-in browser profile.

Risk: Published menus and prices may not reflect current restaurant offerings.

Mitigation: Treat menu details as published information and confirm current offerings and prices with the restaurant when needed.

## Reference(s):

- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge documentation](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured restaurant, menu, availability, reservation, and favorite data with text status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by requested lookup or reservation action; menu details reflect OpenTable's published information.]

## Skill Version(s):

1.4.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
