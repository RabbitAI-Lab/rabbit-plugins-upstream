## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI by routing one-shot requests through the user's signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query easyTable availability, inspect booking areas, dates, and times, find bookings by phone number, and prepare guarded booking-management shell commands without running the easytable MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact booking changes, including real cancellation or creation flows.

Mitigation: Require explicit user confirmation before any cancel, create, or modify request, and do not issue real write calls solely for testing.

Risk: The browser-bridged fpx profile can persist access through a paired browser session.

Mitigation: Use a dedicated browser profile where possible, audit or pin the fpx CLI and Transporter extension, and revoke the pairing after use.

Risk: Booking IDs, phone numbers, Turnstile tokens, and payload values may appear in commands or shell history.

Mitigation: Avoid placing real phone numbers or booking identifiers directly in shell history, and handle harvested tokens as short-lived sensitive data.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and request payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command exit-code interpretation, HTML-fragment parsing guidance, JSONP response handling, and confirmation guidance for write actions.]

## Skill Version(s):

0.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
