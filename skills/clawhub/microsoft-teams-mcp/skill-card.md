## Description:

Helps an agent read Microsoft Teams chats, channels, unread messages, inline images, and the Activity feed from shell scripts using a token captured from a signed-in Teams browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Teams users can use this skill to retrieve chat, channel, unread-message, and Activity feed data from a shell when they need access without running the Microsoft Teams MCP server. A signed-in Teams browser tab is needed to capture the access token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious and cites authenticated write-request capability in read-focused Teams helpers, scope and local image handling concerns, and unresolved local references; its scan is partial.

Mitigation: Restrict helper arguments and write operations to the intended read-only use, clarify tool scope and local image handling, and review unresolved references before installation.

## Reference(s):

- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include chat, channel, unread-message, Activity feed, or inline-image data from the signed-in Teams account.]

## Skill Version(s):

0.8.5 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
