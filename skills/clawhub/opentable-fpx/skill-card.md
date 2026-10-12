## Description:

Helps agents search OpenTable, check availability, and manage reservations and favorites through a signed-in browser session using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using OpenTable can search restaurants, inspect availability and existing reservations, and request bookings, modifications, cancellations, or favorite changes through their signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in session can make real bookings, modifications, cancellations, and favorite changes without an enforced final confirmation.

Mitigation: Prefer read-only use; require the user to review and explicitly approve each account-changing command before execution.

Risk: Bookings or cancellations may involve fees, saved cards, experiences, or 3-D Secure steps.

Mitigation: Review booking details and cancellation terms before acting; involve the user for payment or 3-D Secure steps.

## Reference(s):

- [OpenTable FPX request reference](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)
- [FetchProxy CLI and extension](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return restaurant, availability, reservation, profile, and favorite information from the signed-in account.]

## Skill Version(s):

1.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
