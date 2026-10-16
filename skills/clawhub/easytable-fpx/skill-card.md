## Description:

Guides agents in checking easyTable availability and managing restaurant reservations through browser-backed fpx shell commands without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can check restaurant booking areas, dates, and times, find reservations by phone, and cancel bookings from a shell; creating or modifying bookings requires manual browser steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking lookups and cancellations can affect reservations the user is not authorized to manage.

Mitigation: Use only for reservations you are authorized to manage; browser pairing or challenge clearance does not establish ownership.

Risk: Booking and cancellation requests can change real reservations even when issued as tests.

Mitigation: Do not run write requests as tests; confirm booking details before sending and check the response status afterward.

Risk: Persistent browser bridge pairing and manually copied anti-bot tokens may be misused.

Mitigation: Restrict browser site access, pair only a trusted browser session, and do not share copied tokens.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx on ClawHub](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and booking payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability reads return HTML fragments; booking writes require checking the response status.]

## Skill Version(s):

1.2.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
