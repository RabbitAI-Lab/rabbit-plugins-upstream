## Description:

Guides agents in checking easyTable restaurant availability, finding bookings by phone, and managing bookings through a paired browser session with the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents using easyTable can check restaurant booking areas, dates, and times, locate existing bookings by phone number, and cancel reservations from a shell without an MCP server. Creating or modifying a booking requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paired browser extension and fpx can access the user's easyTable browser context.

Mitigation: Install and pair only if comfortable granting that access, and limit its use to the intended easyTable session.

Risk: Phone numbers, booking IDs, and Turnstile tokens are sensitive booking data.

Mitigation: Keep these values private and avoid exposing them in logs or shared output.

Risk: Create, modify, and cancel requests can change real restaurant reservations.

Mitigation: Obtain explicit user confirmation before each write request; do not test by making live booking changes.

## Reference(s):

- [easyTable requests for fpx](artifact/references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx on ClawHub](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and booking request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read requests return HTML fragments; booking changes require checking the response status.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
