## Description:

Helps agents search OpenTable restaurants and availability, view account details, and manage reservations through a signed-in browser session using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find restaurants and available tables or manage a user's OpenTable reservations from shell-based workflows without running the OpenTable MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw booking, modification, cancellation, and favorites requests can change the signed-in account without an enforced confirmation step.

Mitigation: Require explicit final confirmation before each write action; show restaurant, date, time, party size, cancellation policy, fees, experience price, and saved-card requirement.

Risk: The skill gives an agent direct access to a signed-in OpenTable browser session, including actions involving saved cards.

Mitigation: Install only when that session access is acceptable; prefer the MCP tools when built-in preview and confirmation-token safeguards are needed.

## Reference(s):

- [OpenTable via fpx on ClawHub](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable request examples](artifact/references/opentable-fpx-requests.md)
- [Initial-state extraction helper](artifact/references/extract-initial-state.mjs)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and structured response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read requests may return restaurant or reservation data; write requests may change the signed-in account.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
