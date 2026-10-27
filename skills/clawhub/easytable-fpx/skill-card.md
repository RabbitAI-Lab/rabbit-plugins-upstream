## Description:

Guides agents in checking easyTable availability and finding or cancelling reservations through a paired browser using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check restaurant booking areas, dates, and times, locate reservations by phone number, and cancel authorized bookings without running an MCP server. Creating or modifying a reservation requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cancellation or other write operations can change real reservations without adequate confirmation.

Mitigation: Only manage reservations the user is authorized to manage, and require explicit user confirmation before each create, modify, or cancel command.

Risk: Phone numbers and booking IDs can be exposed in reusable shell history or logs.

Mitigation: Avoid putting real phone numbers or booking IDs in saved commands, shared logs, or reusable shell history.

Risk: The workflow depends on an external CLI and a persistently paired browser extension.

Mitigation: Review the fpx CLI and ContextMint Bridge extension sources before installation, and review the browser pairing before use.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx ClawHub release](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability responses are HTML fragments; cancellation results require checking the returned status. Creating or modifying a booking requires a manually obtained Turnstile token.]

## Skill Version(s):

1.2.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
