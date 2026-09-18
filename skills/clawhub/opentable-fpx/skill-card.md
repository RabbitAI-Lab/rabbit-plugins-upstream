## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including restaurant search, availability checks, reservation listing, favorites, booking, modification, and cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to make OpenTable data and account actions available to an agent or shell workflow without running the OpenTable MCP server. It supports scripted lookup, booking preview, reservation changes, and cancellation workflows that operate through the user's signed-in OpenTable browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give a CLI paired to a signed-in OpenTable browser session authority to read account data and make real reservation changes.

Mitigation: Install only reviewed pinned versions, use a private temporary directory with owner-only permissions, avoid storing tokens or card metadata, and revoke or isolate the browser pairing when it is not actively needed.

Risk: Booking, modification, and cancellation commands can commit changes without an enforced confirmation step.

Mitigation: Require a fresh human confirmation before any write action, preview booking details first, and review cancellation policies, card requirements, same-day conflicts, and experience requirements before execution.

## Reference(s):

- [OpenTable fpx request catalogue](references/opentable-fpx-requests.md)
- [Initial state extractor](references/extract-initial-state.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that read signed-in account data or perform real reservation changes when executed by a paired fpx CLI.]

## Skill Version(s):

0.19.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
