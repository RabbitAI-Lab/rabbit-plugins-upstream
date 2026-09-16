## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI instead of running the opentable-mcp server, including restaurant search, slot availability checks, reservation/favorites listing, and booking, modification, or cancellation through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented users use this skill to issue OpenTable search, availability, profile, reservation, favorite, booking, modification, and cancellation requests through a signed-in browser session when they need scriptable access without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw write commands can book, modify, or cancel real OpenTable reservations without an enforced confirmation step.

Mitigation: Before running write commands, manually verify the exact reservation details and cancellation or payment policy, and run them only when the action is intended.

Risk: The skill acts through the user's signed-in OpenTable browser session.

Mitigation: Install only if this access is acceptable, restrict browser-extension site access, revoke pairing when finished, and prefer a pinned or local install.

Risk: Reservation tokens or account-specific request data can appear in shared shell history or logs.

Mitigation: Avoid storing or printing reservation tokens in shared shells, transcripts, or logs.

## Reference(s):

- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial state extraction helper](references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper code, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act through the user's signed-in OpenTable browser session and may perform real reservation actions.]

## Skill Version(s):

0.19.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
