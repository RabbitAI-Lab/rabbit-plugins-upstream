## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Resy MCP server for restaurant availability search, reservation booking, reservation management, favorites, and Priority Notify subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Resy account credentials to book or cancel real reservations.

Mitigation: Install only if the user is comfortable giving the MCP server their Resy email and password and allowing it to act on their account.

Risk: Cancellation may remove a reservation or trigger cancellation fees.

Mitigation: Require the agent to show the exact reservation and obtain clear confirmation before using cancellation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Resy account credentials and MCP server registration; write actions can book or cancel real reservations.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
