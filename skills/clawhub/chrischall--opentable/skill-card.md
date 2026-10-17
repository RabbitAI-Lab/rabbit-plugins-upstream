## Description:

Helps people find restaurants and published menus, check availability, and manage OpenTable reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners and assistants use this skill to find restaurant menus and open tables, book or change reservations, and manage saved restaurants in an OpenTable account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read account details and act through a signed-in OpenTable browser tab.

Mitigation: Install the server and browser extension only if comfortable granting access to that session, and review what account information is shared.

Risk: Bookings, changes, and cancellations can affect reservations and may incur charges under a restaurant's policy.

Mitigation: Keep confirmation prompts enabled and review the reservation, saved-card details, and cancellation policy before approving each action.

Risk: Adding or removing favorites changes the account immediately.

Mitigation: Confirm the chosen restaurant and obtain the user's approval before changing favorites.

## Reference(s):

- [OpenTable skill release on ClawHub](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text with restaurant details, menus, availability, and reservation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation responses may include confirmation details, cancellation policies, and short-lived booking information.]

## Skill Version(s):

1.3.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
