## Description:

Read Microsoft Teams chats, teams, channels, Activity feed entries, and the currently open chat or channel from a signed-in browser tab using the fpx CLI instead of running the Microsoft Teams MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and run fpx shell commands that extract readable Microsoft Teams data from an already signed-in browser tab for scripting, inspection, or agent workflows. It is useful when the Microsoft Teams MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can surface privacy-sensitive Microsoft Teams messages and activity from the signed-in browser session.

Mitigation: Use it only for Teams data you are authorized to access, and avoid storing or sharing raw message output unless necessary and approved.

Risk: If multiple Teams tabs are open, extraction may read from a different tab than intended.

Mitigation: Close extra Teams tabs and confirm the visible chat, channel, tenant, or Activity view before running extraction commands.

Risk: The workflow depends on the fpx CLI and Transporter browser extension receiving read access to rendered page content.

Mitigation: Install and pair those tools only if trusted, and review declared scopes before approving browser access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [fpx dom-list recipes for Teams](references/dom-list-recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance]

**Output Format:** [Markdown with shell command examples and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only extraction guidance for Teams content already rendered in the browser; command results are typically JSON rows that may contain private Teams messages.]

## Skill Version(s):

0.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
