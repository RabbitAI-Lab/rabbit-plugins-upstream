## Description:

Guides an agent to search OpenTable restaurants and availability and manage reservations through a signed-in browser session using fpx shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners and their agents use this skill to find restaurants, check availability, and manage OpenTable bookings and favorites without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, modification, cancellation, and favorites commands can change a signed-in account immediately without an enforced confirmation step.

Mitigation: Require explicit final user confirmation outside the skill before running any write command; preview booking details and cancellation terms first.

Risk: An agent with an active browser bridge can reuse the signed-in OpenTable session.

Mitigation: Pair only when needed, restrict bridge access, and unpair it when finished.

## Reference(s):

- [OpenTable fpx skill release](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [ContextMint Bridge source and installation](https://github.com/nullnet-app/contextmint-bridge)
- [fpx and browser extension guidance](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may perform live actions on the signed-in OpenTable account.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
