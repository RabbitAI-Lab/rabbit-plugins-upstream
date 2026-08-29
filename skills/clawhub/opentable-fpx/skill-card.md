## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI, including search, slot availability, reservation and favorites listing, and book, modify, or cancel actions through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate OpenTable reservation lookup and account actions from shell workflows when the MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real booking, modification, cancellation, and wishlist actions can run through the user's signed-in OpenTable session without a built-in confirmation gate.

Mitigation: Require explicit human confirmation outside the skill before any mutation command; preview booking details, cancellation policy, conflicts, and saved-card requirements before committing.

Risk: A paired signed-in browser session can expose account data and saved-card-backed reservation capabilities to the agent workflow.

Mitigation: Use only with trusted agents and an intentionally paired browser profile; disable or remove the fpx OpenTable profile when the workflow is no longer needed.

## Reference(s):

- [OpenTable FPX ClawHub listing](https://clawhub.ai/chrischall/skills/opentable-fpx)
- [extract-initial-state.mjs](references/extract-initial-state.mjs)
- [OpenTable requests for fpx](references/opentable-fpx-requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to issue OpenTable GraphQL and REST requests via fpx.]

## Skill Version(s):

0.16.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
