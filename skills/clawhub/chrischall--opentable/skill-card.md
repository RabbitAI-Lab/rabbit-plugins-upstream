## Description:

Helps agents find restaurants and menus, check availability, and manage OpenTable reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners use an agent to explore restaurant menus and availability, book or modify tables, review or cancel reservations, and manage favorites in their OpenTable account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and browser extension use the diner's live signed-in OpenTable session.

Mitigation: Install them only if you trust both components and understand their access to the signed-in session.

Risk: Bookings, changes, cancellations, and favorites can alter the account; some reservations carry cancellation or no-show charges.

Mitigation: Review any applicable policy and payment details, and explicitly confirm account changes before the agent makes them.

## Reference(s):

- [OpenTable skill on ClawHub](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include menu details, availability, reservation confirmations, and cancellation policies.]

## Skill Version(s):

1.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
