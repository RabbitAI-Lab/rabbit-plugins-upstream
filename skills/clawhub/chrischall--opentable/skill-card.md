## Description:

Manage OpenTable restaurant reservations through an MCP server that can search restaurants, check availability, book tables, list or cancel reservations, modify reservations, and manage favorites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to manage their own OpenTable reservations from a signed-in browser session. It helps an agent find restaurant options, inspect slots, preview booking terms, commit or modify reservations, cancel bookings, and maintain saved restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in OpenTable browser session and can change real reservations.

Mitigation: Use it only when comfortable with an MCP server and browser extension acting on the OpenTable account, and require confirmation of restaurant, date, time, party size, policy, and any card hold before booking, modifying, or canceling.

Risk: The security review reports that explicit confirmation is not consistently required before reservation-changing actions.

Mitigation: Configure agent workflows to pause for user confirmation before calling booking, modification, or cancellation tools.

Risk: The skill depends on a browser extension and an authenticated OpenTable tab.

Mitigation: Review the skill carefully before installing and keep the browser session and extension limited to users who intend to grant this reservation-management access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source repository](https://github.com/chrischall/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke MCP tools that read profile and reservation data and can create, modify, or cancel real OpenTable reservations when configured.]

## Skill Version(s):

0.18.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
