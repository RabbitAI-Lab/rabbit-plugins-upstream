## Description:

Manage OpenTable reservations through MCP by searching restaurants, checking availability, booking or canceling tables, listing reservations, and managing favorites with a signed-in OpenTable browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent help with OpenTable reservation workflows, including finding restaurants, checking slots, making or canceling reservations, and managing saved restaurants. It is intended for use only when the required MCP server and fetchproxy browser extension are connected to the user's signed-in OpenTable session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in OpenTable browser session to book, modify, cancel, or favorite restaurants on the user's account.

Mitigation: Require explicit user approval before every account-changing action and show the restaurant, date, time, party size, cancellation terms, and any card hold details before committing.

Risk: Trust depends on the external opentable-mcp package and fetchproxy browser extension.

Mitigation: Review and install those components deliberately, and treat their publisher, version, and update path as part of the security decision.

Risk: The skill relies on the user's active OpenTable browser session for authentication.

Mitigation: Use it only in a browser profile controlled by the user and reauthenticate directly on opentable.com when the session expires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke MCP tools that read or change the user's OpenTable account when connected to a signed-in browser session.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
