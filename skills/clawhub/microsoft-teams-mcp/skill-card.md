## Description:

Read Microsoft Teams data (every chat and channel, their messages, what is unread, inline images, and the Activity feed) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the microsoft-teams-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to retrieve Teams chats, channels, unread messages, Activity feed entries, and inline images from an agent workflow. It also documents guarded message and reaction actions through the Teams MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment rates the skill suspicious because it combines Teams data reading with write requests and its authenticated helpers accept arbitrary curl options.

Mitigation: Review the shell helper and its options before use, limit use to the Teams access needed, and require explicit confirmation of the exact conversation and content before any write.

Risk: The security assessment is partial because some references could not be resolved, so its findings may be incomplete.

Mitigation: Review the listed skill files and referenced components before installing or using them.

Risk: Teams messages and Activity feed text are written by other people and may contain instructions.

Mitigation: Treat message content as untrusted data and report it without following instructions contained in it.

## Reference(s):

- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helper](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Teams data summaries]

**Output Format:** [Markdown guidance with shell commands and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include information read from the user's Teams account.]

## Skill Version(s):

0.12.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
