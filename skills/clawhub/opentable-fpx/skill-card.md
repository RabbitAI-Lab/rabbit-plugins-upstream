## Description:

opentable-fpx helps agents use the fpx CLI to search OpenTable, inspect availability, manage favorites and reservations, and perform booking, modification, or cancellation actions through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to issue shell-based OpenTable queries and reservation workflows without running the OpenTable MCP server. It is intended for workflows where the user has a signed-in OpenTable browser session available through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real OpenTable booking, modification, cancellation, favorite-change, and saved-card-backed reservation actions through a signed-in browser session.

Mitigation: Require explicit user confirmation before write actions, and verify the restaurant, date, time, party size, cancellation fees, credit-card requirements, and saved-card use before execution.

Risk: Raw fpx request recipes do not provide the confirm gate used by the corresponding MCP tools.

Mitigation: Use a preview step in the surrounding workflow and treat booking, modification, cancellation, and favorite changes as account-changing operations.

## Reference(s):

- [OpenTable requests for fpx](references/opentable-fpx-requests.md)
- [Initial state extractor](references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, jq filters, and a helper JavaScript file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill outputs command recipes and request payloads for use with fpx; write operations act on the user's signed-in OpenTable account.]

## Skill Version(s):

0.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
