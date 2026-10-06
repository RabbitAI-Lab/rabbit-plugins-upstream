## Description:

Guides agents using the fpx CLI to check easyTable availability, find bookings by phone, and cancel bookings through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can check restaurant booking areas, dates, and times, find reservations by phone, and cancel bookings without running an MCP server. Creating or modifying bookings requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-guided commands through a paired browser can change live restaurant bookings.

Mitigation: Review bridge pairing and require explicit human confirmation before cancellation, creation, or modification; do not test with real write requests.

Risk: Creating or modifying bookings involves reuse of a browser anti-bot token.

Mitigation: Review the token-handling workflow before installation and use it only for the intended booking action.

## Reference(s):

- [easyTable request examples](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx release](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read requests return HTML fragments; cancellations return JSONP. Creating or modifying bookings requires a manually obtained browser token.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
