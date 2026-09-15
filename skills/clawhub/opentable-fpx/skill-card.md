## Description:

Query and manage OpenTable (opentable.com) restaurant reservations from a shell with the fpx CLI (@fetchproxy/cli) instead of running the opentable-mcp server: search restaurants, check slot availability, list reservations/favorites, and book/modify/cancel a table via one-shot GraphQL and REST calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to script OpenTable lookup and account actions from a shell when they want one-shot fpx calls instead of running an MCP server. It supports restaurant search, availability checks, reservation/profile/favorites reads, and booking, modification, cancellation, and favorites writes through the user's signed-in OpenTable browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make, change, or cancel real OpenTable reservations through the user's signed-in browser session without an enforced confirmation step.

Mitigation: Prefer MCP tools with preview and confirm:true for real booking or cancellation actions; when using fpx directly, preview booking details and cancellation policies before any write.

Risk: The browser bridge effectively grants access to the user's OpenTable account and may involve reservation or card-token data.

Mitigation: Treat the bridge as account access, use private temporary files, avoid logging reservation or card-token data, and disconnect browser pairing when finished.

Risk: The workflow depends on the fpx CLI package and a paired browser extension.

Mitigation: Pin and verify the fpx package before use and check bridge health before issuing requests.

## Reference(s):

- [OpenTable FPX request catalogue](references/opentable-fpx-requests.md)
- [Initial state extraction script](references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, JSON request bodies, jq filters, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that perform real OpenTable account actions through a signed-in browser session.]

## Skill Version(s):

0.19.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
