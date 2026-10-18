## Description:

Guides agents through searching and managing OpenTable reservations with shell commands using a signed-in browser session instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search restaurants and availability, inspect their reservations and favorites, and prepare or execute bookings, modifications, and cancellations through their signed-in OpenTable session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, modification, or cancellation commands can change real reservations without a built-in final confirmation.

Mitigation: Require explicit human confirmation for each write; review the restaurant, date, party size, and cancellation target before execution.

Risk: Bookings may carry cancellation fees, card requirements, or other conditions tied to the signed-in account.

Mitigation: Inspect booking details and the cancellation policy, card or fee requirements, and any Experience terms before confirming a booking or change.

## Reference(s):

- [OpenTable requests for fpx](artifact/references/opentable-fpx-requests.md)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)
- [OpenTable via fpx on ClawHub](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an existing signed-in OpenTable browser session; write commands affect live reservations.]

## Skill Version(s):

1.3.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
