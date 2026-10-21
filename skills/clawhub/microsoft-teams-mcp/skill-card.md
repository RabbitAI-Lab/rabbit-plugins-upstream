## Description:

Retrieves Microsoft Teams chats, channels, unread messages, inline images, and Activity feed data from a shell without running the Teams MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can retrieve Teams conversations, unread messages, inline images, and Activity feed data from shell workflows when the Teams MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read helpers may permit changes or send the saved access token to unchecked destinations.

Mitigation: Use helpers that reject arbitrary curl options and validate every destination; require approval for messages and reactions.

Risk: The integration accesses private Teams conversations and stores a reusable access token.

Mitigation: Limit access to the token and conversation data; when removing the skill, revoke the browser pairing and delete the cached token.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Chat-service recipes](references/chatsvc-recipes.md)
- [Teams chat-service helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and shell snippets; retrieved Teams data as JSON or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved content may include private conversation messages and inline images.]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
