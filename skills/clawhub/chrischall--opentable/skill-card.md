## Description:

Manage OpenTable reservations via MCP by searching restaurants, checking availability, booking or canceling tables, modifying reservations, and managing favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform OpenTable restaurant discovery and reservation tasks. It supports searching venues, checking slots, booking, modifying or canceling reservations, viewing profile and reservation data, and managing favorite restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on unpinned external software for the MCP server and browser extension.

Mitigation: Install only after reviewing and trusting the package and extension publisher, and prefer a reviewed or pinned installation source when deploying in managed environments.

Risk: The browser extension uses a signed-in OpenTable session and can expose profile, reservation, and favorites data to the agent context.

Mitigation: Use a browser profile intended for this workflow, review requested actions before execution, and avoid exposing the agent context to untrusted parties.

Risk: Booking, modification, cancellation, favorites, and card-hold actions can change a user's OpenTable account or reservation state.

Mitigation: Require explicit user confirmation before committing booking, modification, cancellation, favorite changes, or any action involving a card hold or cancellation policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source repository](https://github.com/chrischall/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, JSON configuration examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OpenTable reservation details, confirmation numbers, security tokens, cancellation policies, saved card last-four details for holds, and compact or full MCP response views.]

## Skill Version(s):

0.19.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
