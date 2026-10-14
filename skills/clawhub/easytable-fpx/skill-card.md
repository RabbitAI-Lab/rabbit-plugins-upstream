## Description:

Guides agents through checking easyTable restaurant availability and managing reservations with shell commands routed through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can check restaurant booking areas, dates, and times, find reservations by phone, and cancel authorized bookings from a shell. Creating or modifying a booking requires a manual browser step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-session access to protected easyTable endpoints may expose reservation information.

Mitigation: Review the external CLI and browser extension before pairing, and use only a browser session you are authorized to operate.

Risk: Cancellation, creation, or modification can change a real restaurant booking.

Mitigation: Confirm authorization and booking details before any write; do not send live writes merely to test the flow.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easytable-fpx release](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and example booking payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Create and modify flows require a manual browser step; booking writes can affect real reservations.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
