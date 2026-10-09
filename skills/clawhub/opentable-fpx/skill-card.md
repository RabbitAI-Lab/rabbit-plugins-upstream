## Description:

Helps agents search OpenTable restaurants and availability, review reservations and favorites, and manage bookings through a signed-in browser session using fpx commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents managing an OpenTable account can look up restaurants and available tables, then prepare or perform reservation and favorites actions using their signed-in session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can book, modify, or cancel real reservations and change favorites without a built-in final confirmation gate.

Mitigation: Before each account-changing command, show the restaurant, date, time, party size, fees, card requirement, and cancellation policy; require explicit user approval before execution.

Risk: Paired shell access can use the user's signed-in OpenTable session.

Mitigation: Install only if comfortable granting that access, and remove or revoke the pairing when it is no longer needed.

## Reference(s):

- [OpenTable via fpx on ClawHub](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [OpenTable request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and structured reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and account-change commands act on the user's signed-in OpenTable session.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
