## Description:

Guides agents in reading Microsoft Teams chats, channels, unread messages, inline images, and the Activity feed using a signed-in browser session and shell tools instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized Teams users can ask an agent to retrieve chats, channel messages, unread activity, and inline images from their signed-in account without running the Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access sensitive Teams chats and activity through the user's session.

Mitigation: Grant access only when appropriate and share only the information requested.

Risk: A usable Teams bearer token is saved locally and unreviewed extra curl arguments could expose it.

Mitigation: Treat ~/.teams-fpx/curlrc as sensitive session material, remove it when done, and never pass unreviewed or user-controlled extra curl arguments to the helpers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and summaries of requested Teams data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include sensitive Teams messages and activity; shared-file downloads and Calendar access are outside this skill.]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
