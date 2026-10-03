## Description:

Guides agents through checking easyTable availability, finding bookings by phone, and cancelling reservations using the fpx CLI through a browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use this skill to check restaurant booking areas, dates, and times, look up an existing reservation, and cancel it without running an MCP server. Creating or modifying reservations requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change or cancel real restaurant reservations.

Mitigation: Require explicit user confirmation before any create, modify, or cancel command; do not test with real writes.

Risk: Browser-bridged requests depend on a third-party extension and CLI running in the user's browser context.

Mitigation: Verify the extension and package source before installation and scope the browser profile to easytable.com.

Risk: Booking details and short-lived Turnstile tokens can be exposed in commands or logs.

Mitigation: Keep phone numbers, booking details, and Turnstile tokens out of shared logs and transcripts.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and example JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability reads return HTML fragments; cancellation responses must be checked for success in the response body.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
