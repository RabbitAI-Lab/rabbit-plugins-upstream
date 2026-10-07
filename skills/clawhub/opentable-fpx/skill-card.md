## Description:

Helps agents search restaurants, check availability, and manage OpenTable reservations and favorites using a signed-in browser session and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents managing restaurant plans can find tables, review booking details, and make, change, or cancel reservations through the user's signed-in OpenTable session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, changing, cancelling, or favoriting can take effect on the signed-in account without an enforced confirmation step.

Mitigation: Before each action, require explicit user approval after showing the restaurant, time, party size, fees, cancellation policy, card involvement, and exact action.

Risk: A persistent browser pairing can continue to expose the signed-in OpenTable session to agent actions.

Mitigation: Keep the pairing active only for the time needed to complete the requested task.

## Reference(s):

- [OpenTable via fpx on ClawHub](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable request catalogue](artifact/references/opentable-fpx-requests.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension guidance](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the user's signed-in OpenTable browser session; write actions take effect immediately.]

## Skill Version(s):

1.3.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
