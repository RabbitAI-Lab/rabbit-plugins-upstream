## Description:

Snag hard-to-get tables on Resy by monitoring cancellations or attempting scheduled reservation releases, then automatically booking a table that matches the diner's authorized preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bondseat](https://clawhub.ai/user/bondseat)

### License/Terms of Use:

MIT-0

## Use Case:

External diners and their agents use BondSeat to request, monitor, schedule, check, stop, or resume Resy reservation-booking work within explicit restaurant, date, party-size, and time-window instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses stored Resy connection state and other connector state that can include sensitive credentials or tokens.

Mitigation: Use one private persistent state file per diner and environment, isolate storage on multi-user hosts, and do not read, display, or attach the state file.

Risk: The skill can automatically book a reservation and trigger the disclosed successful-booking fee when authorized details match.

Mitigation: Authorize only exact restaurant, date, party-size, and time-window details the diner is willing to have booked automatically, and disclose the $10 successful-booking fee before submission.

Risk: Background checks and reservation attempts can become excessive if the agent ignores returned polling intervals or contacts provider APIs directly.

Mitigation: Follow returned polling delays, schedule status checks no more than once per minute, and use BondSeat's connector instead of directly polling Resy or OpenTable APIs.

Risk: A provider result can be unconfirmed, so incorrectly reporting success or failure could mislead the diner.

Mitigation: For unconfirmed provider outcomes, ask the diner to check their provider reservations and end automatic follow-up instead of claiming a final booking state.

## Reference(s):

- [BondSeat agents homepage](https://bond-seat.com/agents)
- [BondSeat ClawHub skill page](https://clawhub.ai/bondseat/skills/bondseat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON connector inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and npx; uses a private persistent state file per diner for connection state.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
