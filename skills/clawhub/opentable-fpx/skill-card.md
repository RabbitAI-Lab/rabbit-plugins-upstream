## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot availability checks, reservation and favorites listing, and booking, modifying, or canceling tables through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to generate shell-based OpenTable workflows for searching restaurants, checking availability, reading account reservation data, and performing reservation actions without running the OpenTable MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can book, modify, cancel, or change favorites in the user's real OpenTable account.

Mitigation: Preview reservation details, cancellation policies, saved-card requirements, and target reservation identifiers before running write commands.

Risk: The fpx/Transporter setup uses the user's signed-in OpenTable browser session.

Mitigation: Install and pair the skill only when the user accepts giving the workflow access to that active session.

Risk: Credit-card-required slots, cancellation fees, 3-D Secure, and same-day conflicts may affect booking outcomes.

Mitigation: Fetch booking details first, inspect policy and wallet fields, and stop for browser-based completion when 3-D Secure is required.

## Reference(s):

- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extraction helper](references/extract-initial-state.mjs)
- [OpenTable website](https://www.opentable.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON request bodies, jq filters, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that perform real OpenTable account actions through the user's signed-in browser session.]

## Skill Version(s):

0.16.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
