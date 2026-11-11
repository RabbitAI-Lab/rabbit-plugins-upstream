## Description:

Use shell-based helpers to read Microsoft Teams chats, channels, unread messages, inline images, and the Activity feed through Teams' chat service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill to inspect Microsoft Teams conversations and activity from a shell, including when the Teams MCP server is unavailable. It provides setup instructions and reusable commands for reading chat and channel data through an authenticated Teams session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes authenticated write requests that could send messages or reactions, and shell use may lack a confirmation step.

Mitigation: Review the write guidance before use; require explicit approval after showing the exact conversation and message before any post, and do not retry a timed-out send without checking the conversation.

Risk: Attacker-controlled arguments may cause unsafe requests or expose credentials.

Mitigation: Do not pass untrusted arguments to the helper, and review the helper behavior and destination handling before execution.

## Reference(s):

- [Teams chat-service recipes](artifact/references/chatsvc-recipes.md)
- [Teams shell helper](artifact/references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve chat and channel data, unread messages, activity, and inline images.]

## Skill Version(s):

0.11.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
