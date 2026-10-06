## Description:

Guides agents in reading chats, channels, and activity from an already signed-in Microsoft Teams browser tab using read-only shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers with authorized access use this skill to inspect Teams chats, channel posts, team lists, and activity in a signed-in browser tab from a shell, without running a Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted Teams messages, names, and activity can contain confidential business or personal information.

Mitigation: Use only with authorized workspace access, and avoid saving or sharing sensitive command output.

Risk: Multiple open Teams tabs can cause data to come from an unintended conversation.

Mitigation: Close extra Teams tabs and confirm the open conversation before relying on extracted messages.

Risk: Browser pairing grants access to the declared DOM selector scope.

Mitigation: Review the declared selector scope before approving bridge pairing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams DOM-list recipes](references/dom-list-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; results depend on the active Teams tab and currently displayed view.]

## Skill Version(s):

0.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
