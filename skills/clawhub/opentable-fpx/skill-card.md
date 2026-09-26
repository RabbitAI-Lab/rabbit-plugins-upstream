## Description:

Helps agents search OpenTable restaurants and availability, review reservations and favorites, and manage bookings through a signed-in browser session using fpx shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find restaurants, check table availability, and manage OpenTable reservations from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can book, modify, or cancel reservations without an enforced confirmation step, potentially involving saved cards or cancellation fees.

Mitigation: Before any write command, require explicit approval after showing the exact restaurant, date and time, party size, target reservation, policy, and any fee or card implications.

## Reference(s):

- [OpenTable via fpx release](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extraction utility](references/extract-initial-state.mjs)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use an authenticated OpenTable browser session; write operations act on the live account.]

## Skill Version(s):

1.2.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
