## Description:

Helps agents check easyTable restaurant availability, find bookings by phone number, and cancel reservations through a paired browser using fpx instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can use an agent to inspect restaurant booking areas, dates, and times, look up their reservations, and cancel them without running an MCP server. Creating or changing a booking requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking lookup by phone number can disclose personal reservation details.

Mitigation: Look up only reservations you are authorized to manage and avoid saving phone numbers or booking details in reusable files or shell history.

Risk: Cancel, create, and modify commands can change real restaurant reservations.

Mitigation: Confirm the reservation and intended action before any write; never run write examples as tests.

Risk: Live requests rely on a paired browser extension and fpx CLI.

Mitigation: Review these tools before installation and use a browser session you control.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx on ClawHub](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability and booking lookups are read-only; cancellation changes a live reservation. Creating or modifying a booking requires a manual browser step.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
