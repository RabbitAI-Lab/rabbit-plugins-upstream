## Description:

Helps an agent search OpenTable, check availability, and manage reservations and favorites through a signed-in browser session using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents using a signed-in OpenTable account can find restaurants and tables, review upcoming reservations, and prepare or perform booking, modification, cancellation, and favorite changes from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, modification, cancellation, and favorite changes can take effect without an enforced confirmation checkpoint.

Mitigation: Before any write, show the exact restaurant, time, party size, policy, fees, card requirement, and proposed action; wait for explicit user approval before running the command.

Risk: The agent operates through the user's signed-in OpenTable browser session, including reservations that may require a saved card.

Mitigation: Use the skill only if the user accepts signed-in account access; review booking details and card requirements before approving a reservation.

## Reference(s):

- [OpenTable fpx skill release](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands return restaurant and reservation data; write commands can change the signed-in account.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
