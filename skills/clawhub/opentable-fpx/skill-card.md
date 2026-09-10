## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, slot checks, reservation and favorite lookup, and booking, modification, or cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to perform OpenTable reservation workflows from shell commands when the OpenTable MCP server is unavailable or a one-shot CLI workflow is preferred. It is suitable for reading restaurant and account data and for carefully reviewed booking, modification, favorite, and cancellation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated fpx commands can book, modify, cancel, favorite, or lock OpenTable reservations without an enforced confirmation step.

Mitigation: Require explicit human review of the exact restaurant, date, time, party size, action, and request body before running any write command.

Risk: Commands operate through the user's signed-in OpenTable session and may access account, reservation, saved card, or policy details.

Mitigation: Use the skill only with an intended signed-in session, limit browser extension site access to OpenTable, and revoke the browser pairing when finished.

Risk: Booking flows can involve cancellation fees, credit-card requirements, 3-D Secure, same-day conflicts, Experience requirements, or regional shard failures.

Mitigation: Fetch and review booking details, cancellation policy, card requirements, conflicts, and region-specific behavior before slot-lock, booking, modification, or cancellation.

Risk: Example workflows write request and response data to fixed temporary paths that may expose reservation or account details on shared systems.

Mitigation: Prefer private temporary files, restrictive permissions, or streaming pipelines for any data containing profile, reservation, payment, or token fields.

## Reference(s):

- [OpenTable FPX request catalog](artifact/references/opentable-fpx-requests.md)
- [OpenTable initial-state extractor](artifact/references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read account data or trigger real OpenTable reservation actions through the user's signed-in browser session.]

## Skill Version(s):

0.19.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
