## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, reservation lookup and cancellation, favorites, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Resy restaurant reservation workflows after the user configures the required MCP server and credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent authenticated authority to book or cancel reservations and change account-related Resy state.

Mitigation: Use only clear user-directed prompts and require explicit confirmation before booking, cancelling, changing favorites, or subscribing to Priority Notify.

Risk: The MCP server requires Resy email and password credentials.

Mitigation: Configure credentials only for trusted MCP clients, store them as environment secrets, and review whether account access is acceptable before installation.

Risk: The underlying Resy integration uses private web-app endpoints rather than an official public API.

Mitigation: Expect endpoint behavior to change and review failures or unexpected actions before relying on the skill for reservation management.

## Reference(s):

- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp GitHub project](https://github.com/chrischall/resy-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide or invoke authenticated Resy MCP actions when the MCP server is installed and configured.]

## Skill Version(s):

0.9.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
