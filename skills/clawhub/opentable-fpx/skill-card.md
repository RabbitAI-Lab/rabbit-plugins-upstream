## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot availability, reservations, favorites, and booking, modification, or cancellation through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect OpenTable data and generate fpx commands for reservation workflows without running the OpenTable MCP server. It is intended for shell-based use with a signed-in OpenTable browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutating fpx commands can create, modify, cancel, or favorite OpenTable reservations without an enforced final confirmation step.

Mitigation: Require the agent to show the exact restaurant, date, time, party size, seating or experience, cancellation terms, fees, and saved-card implications, then obtain explicit approval in chat before running any mutating command.

Risk: The skill uses the user's signed-in OpenTable browser session, including loyalty account state and saved-card flows.

Mitigation: Install and run it only when this session access is acceptable, keep Transporter site access scoped to opentable.com, and review account and card implications before booking.

Risk: OpenTable constraints such as credit-card-required slots, 3-D Secure, Experience requirements, same-day conflicts, and non-NA database regions can make generated commands fail or have unintended booking consequences.

Mitigation: Fetch the booking details page before committing, inspect cancellation policy, card requirements, conflicts, dining area, and Experience data, and rerun discovery steps when a lock expires or a persisted query changes.

## Reference(s):

- [OpenTable fpx request catalogue](artifact/references/opentable-fpx-requests.md)
- [Initial state extractor](artifact/references/extract-initial-state.mjs)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with shell commands, JSON request bodies, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act through the user's signed-in OpenTable browser session and can perform real account-changing actions.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
