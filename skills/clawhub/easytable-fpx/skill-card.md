## Description:

Guides agents to check easyTable availability, find and cancel reservations, and prepare manual-assisted booking requests using the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using easyTable can check restaurant booking areas, dates, and times, look up reservations by phone number, and cancel bookings through their paired browser session without running an MCP server. Creating or modifying a booking requires a manual step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, modify, and cancel commands can change real restaurant bookings.

Mitigation: Confirm the restaurant, reservation, and intended action before executing a write; do not test with live booking changes, and check the returned status.

Risk: The CLI and browser extension act through the user's easyTable browser session.

Mitigation: Verify the external CLI and extension sources before installation and pairing, and only pair a browser session you intend to use.

Risk: The manual Turnstile-token workaround may have site-policy implications.

Mitigation: Avoid the workaround unless you understand the implications; treat create and modify as manual-assisted rather than one-shot operations.

## Reference(s):

- [easytable-fpx release](https://clawhub.ai/chrischall/skills/easytable-fpx)
- [easyTable request recipes](references/easytable-requests.md)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability responses include HTML fragments; booking actions require checking the response status.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
