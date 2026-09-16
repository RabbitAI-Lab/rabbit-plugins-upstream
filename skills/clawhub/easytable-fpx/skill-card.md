## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, finding bookings by phone, and cancelling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with easyTable booking widgets through fpx shell commands when the easytable MCP server is unavailable or unnecessary. It supports availability lookup, booking lookup by phone, and cancellation workflows, with create and modify described as manual or hybrid flows because fpx cannot harvest the required Turnstile token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad browser-bridge CLI with a persistent pairing.

Mitigation: Review before installing, use a dedicated browser profile, avoid global unpinned installs where possible, and remove or unpair the fpx profile after use.

Risk: Booking lookup and cancellation workflows may process personal data such as phone numbers, names, booking IDs, and tokens.

Mitigation: Avoid storing these values in shared /tmp files, shell history, or logs.

Risk: Create, modify, and cancel commands can affect real restaurant bookings.

Mitigation: Run these commands only with explicit user intent and verify response status rather than relying only on HTTP success or process exit code.

## Reference(s):

- [easyTable request recipes for fpx](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Code]

**Output Format:** [Markdown with inline shell and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include real booking lookup or cancellation commands and require user review before execution.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
