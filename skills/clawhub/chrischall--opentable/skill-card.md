## Description:

Helps agents find OpenTable restaurants and menus, check availability, and manage reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents can discover restaurants and published menus, find tables, and book, modify, or cancel reservations and manage favorites in their OpenTable account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bridge can act through a signed-in OpenTable tab and change reservations or favorites.

Mitigation: Install only if comfortable granting this access, and confirm booking, modification, and cancellation details before proceeding.

Risk: A booking may carry a card hold or cancellation fee.

Mitigation: Review the saved card and cancellation policy before confirming a booking or modification.

Risk: Reservation and profile outputs can contain sensitive account details.

Mitigation: Avoid sharing confirmation numbers, security tokens, profile information, or saved-card last four digits.

## Reference(s):

- [OpenTable skill listing](https://clawhub.ai/chrischall/skills/opentable)
- [ContextMint Bridge setup](https://github.com/nullnet-app/contextmint-bridge)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses and structured reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation results may include confirmation numbers, security tokens, profile information, or saved-card last four digits.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
