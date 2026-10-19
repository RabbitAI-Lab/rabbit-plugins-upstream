## Description:

Helps an agent search OpenTable restaurants and availability and manage reservations and favorites through a signed-in browser session using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents using OpenTable can find restaurants and available tables, inspect existing reservations, and request booking, modification, cancellation, or favorite changes without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in account actions can book, change, or cancel reservations and alter favorites without an enforced final confirmation.

Mitigation: Before every write, show the exact action, restaurant, time, party size, cancellation policy, and any card or fee terms; obtain explicit approval outside the command flow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable request examples](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an active signed-in OpenTable browser session.]

## Skill Version(s):

1.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
