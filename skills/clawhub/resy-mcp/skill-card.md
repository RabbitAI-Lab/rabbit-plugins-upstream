## Description: <br>
Manage Resy restaurant reservations via MCP: search venues, book tables, list and cancel reservations, manage favorites, and subscribe to Priority Notify. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Resy restaurant reservations through an MCP server, including availability search, booking, cancellation, favorites, and Priority Notify subscriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can book or cancel real restaurant reservations using Resy account credentials. <br>
Mitigation: Require explicit user confirmation before any booking, cancellation, or account-state change, especially when fees or policy consequences may apply. <br>
Risk: The skill requires Resy email and password credentials in the MCP configuration. <br>
Mitigation: Use only a Resy account the agent is intended to manage and keep credentials scoped to this MCP server configuration. <br>
Risk: The artifact states that Resy does not publish an official API and that some endpoint paths are reverse-engineered. <br>
Mitigation: Review carefully before installation and verify behavior against the user's account before relying on booking, cancellation, favorites, or Priority Notify actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-mcp) <br>
- [npm package](https://www.npmjs.com/package/resy-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to call MCP tools that search, book, cancel, or modify Resy account state.] <br>

## Skill Version(s): <br>
0.6.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
