## Description:

Manage OpenTable reservations via MCP, including restaurant search, slot availability, booking, reservation cancellation, and favorites management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage OpenTable dining plans through a signed-in browser session, including finding restaurants, checking availability, booking or changing reservations, canceling reservations, and managing saved restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in OpenTable browser session to book, modify, cancel, or change favorites in a real user account.

Mitigation: Require explicit user confirmation before any state-changing action, restating the restaurant, date, time, party size, policy, card or no-show implications, and requested change.

Risk: Bookings with card holds or no-show fees may have financial consequences.

Mitigation: Use the preview flow when available and show the cancellation policy and saved payment last-four details before committing.

Risk: The security verdict is suspicious because final confirmation is not clearly required for real reservation changes.

Mitigation: Review carefully before installing and constrain the agent to ask for confirmation before booking, modifying, canceling, or changing favorites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source repository](https://github.com/chrischall/opentable-mcp)
- [fetchproxy extension source repository](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, MCP tool calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses short-lived reservation and booking tokens; authenticated actions depend on a signed-in opentable.com browser tab.]

## Skill Version(s):

0.18.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
