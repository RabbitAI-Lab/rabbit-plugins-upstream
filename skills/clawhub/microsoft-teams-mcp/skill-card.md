## Description:

Helps agents read chat lists, messages, teams, channels, posts, and activity from a signed-in Microsoft Teams browser tab using shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers with authorized access use this skill to inspect Teams conversations, channel posts, and activity from a signed-in browser session without deploying an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat, post, and activity output can expose confidential Teams content.

Mitigation: Use only with authorization for the account and workspace; do not store or share exports without organizational permission.

Risk: An unrelated open Teams tab may supply data from an unintended conversation.

Mitigation: Close unrelated Teams tabs and confirm the selected conversation before using extracted records.

Risk: Browser pairing grants the extension access to Teams content beyond the immediate read.

Mitigation: Approve access only when needed and revoke the ContextMint Bridge grant when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams DOM list recipes](references/dom-list-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown instructions and shell commands for reading structured Teams records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; results depend on the open Teams tab and currently selected browser view.]

## Skill Version(s):

0.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
