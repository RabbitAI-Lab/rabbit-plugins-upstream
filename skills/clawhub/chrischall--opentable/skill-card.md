## Description:

Manage OpenTable reservations via MCP: search restaurants, check availability, book tables, list or cancel reservations, and manage favorites using an installed opentable-mcp server and signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent help find restaurants, inspect available reservation slots, book or modify tables, cancel upcoming reservations, and manage OpenTable favorites through the user's signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through a signed-in OpenTable browser session to create, modify, or cancel real reservations.

Mitigation: Require explicit user confirmation before committing booking, modification, or cancellation actions, and restate the restaurant, date, time, party size, and confirmation details.

Risk: Some bookings may involve card holds, cancellation policies, or no-show fees.

Mitigation: Use preview flows before committing and surface any cancellation policy, card hold, saved-card last four digits, and no-show-fee details for user confirmation.

Risk: The MCP server and browser extension operate through the user's authenticated browser tab.

Mitigation: Install only after reviewing the third-party MCP and fetchproxy extension, and keep the browser session under the user's control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source](https://github.com/chrischall/opentable-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger MCP tool calls that search restaurants, preview bookings, commit reservations, modify reservations, cancel reservations, or manage favorites.]

## Skill Version(s):

0.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
