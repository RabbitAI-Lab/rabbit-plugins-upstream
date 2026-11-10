## Description:

Use shell helpers to inspect Teams chats, channels, unread messages, inline images, and the Activity feed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill to inspect their Teams conversations, channels, unread messages, images, and notifications from shell workflows when they need Teams data without the MCP server. It requires a signed-in Teams browser tab to capture an access token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell requests can send messages or change reactions, even though the skill is presented as read-focused.

Mitigation: Require explicit user approval after showing the exact conversation and message before any post; prefer the confirm-gated Teams MCP tools for writes.

Risk: The security review is rated suspicious with medium confidence, and some reference analysis is incomplete.

Mitigation: Review the skill and its references before installation, and install only if the reported capabilities are understood and accepted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [Teams chat-service recipes](artifact/references/chatsvc-recipes.md)
- [Teams shell helpers](artifact/references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; Teams results may be text or image data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the signed-in user's Teams account and the conversations they can access.]

## Skill Version(s):

0.10.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
