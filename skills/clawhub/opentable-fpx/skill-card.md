## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, availability checks, reservation and favorite listing, and booking, modification, or cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-minded OpenTable users use this skill to issue fpx shell commands for restaurant search, availability checks, account reservation and favorite review, and reservation changes without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in OpenTable browser session gives the agent authority to read account details and perform reservation actions.

Mitigation: Install only if this account access is acceptable, and remove the fpx/Transporter pairing when it is no longer needed.

Risk: Booking, modification, cancellation, and saved-card-backed reservation calls can commit real actions without a built-in confirmation gate.

Mitigation: Require a preview and explicit human confirmation before any write action, and review booking details, cancellation policy, card requirements, fees, conflicts, and Experience requirements before committing.

## Reference(s):

- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial state extractor](references/extract-initial-state.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in OpenTable browser session and fpx/Transporter pairing; write actions can affect real reservations.]

## Skill Version(s):

0.19.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
