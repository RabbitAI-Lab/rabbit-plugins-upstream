## Description:

Manage OpenTable reservations through MCP by searching restaurants, checking slot availability, booking tables, listing or canceling reservations, and managing favorites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent find restaurants, inspect OpenTable availability, make or modify reservations, cancel reservations, and manage saved restaurants through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through a signed-in OpenTable account to book, modify, cancel, and change saved restaurants.

Mitigation: Require explicit user confirmation before every booking, cancellation, modification, or favorite change.

Risk: Some bookings can involve cancellation policies or saved-card holds.

Mitigation: Use the preview step and show the cancellation policy and saved-card hold details before committing the booking or modification.

Risk: The skill can read profile and reservation information from the signed-in OpenTable session.

Mitigation: Install and use it only when the user accepts that account data will be available to the agent during reservation workflows.

## Reference(s):

- [ClawHub opentable skill listing](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable website](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue MCP tool calls that search restaurants, inspect account data, preview booking policies, and commit reservation or favorite changes after user approval.]

## Skill Version(s):

1.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
