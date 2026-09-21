## Description:

Query and manage OpenTable restaurant reservations from a shell with the fpx CLI instead of running the opentable-mcp server: search restaurants, check slot availability, list reservations and favorites, and book, modify, or cancel a table through one-shot GraphQL and REST calls using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query OpenTable availability and manage reservations through fpx shell calls against a signed-in browser session, especially when the MCP server is unavailable or undesired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real OpenTable booking, modification, cancellation, favorite, and saved-card-related actions through a signed-in browser session without an enforced confirmation gate.

Mitigation: Require the agent to present the exact restaurant, time, party size, fees, cancellation policy, card use, and reservation identifier, then obtain explicit user approval before any final write action.

Risk: Saved-card-required reservations and cancellation-fee policies may create financial or account-impacting consequences.

Mitigation: Fetch and review the booking details page before committing, including credit-card requirements, saved-card use, cancellation policy, and any Experience terms.

Risk: OpenTable constraints such as same-day conflicts, 3-D Secure requirements, slot-lock expiration, and non-NA database shards can cause booking or cancellation failures.

Mitigation: Check reservation conflicts and booking details first, complete 3-D Secure in a real browser when required, refresh expired slot locks, and treat non-NA shard failures as a known limitation.

## Reference(s):

- [OpenTable FPX request catalogue](references/opentable-fpx-requests.md)
- [Initial state extractor](references/extract-initial-state.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's signed-in OpenTable browser session through fpx and may cause real account actions when write commands are executed.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
