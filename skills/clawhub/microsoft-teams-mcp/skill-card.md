## Description:

Helps agents read Microsoft Teams chats, channels, unread messages, inline images, and the Activity feed from a shell without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Teams users can retrieve conversations, unread messages, Activity notifications, and inline images through shell commands when they do not want to run the Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad curl arguments could send the captured Teams bearer token outside intended Teams endpoints.

Mitigation: Review commands before running them; never pass message content, untrusted URLs, or generated text as extra curl arguments to the helpers.

Risk: A cached bearer token can expose the user's Teams data if the local cache is accessed or retained unnecessarily.

Mitigation: Protect the local token cache and refresh or delete ~/.teams-fpx/curlrc when access is no longer wanted.

Risk: Teams messages may contain instructions from other people, and writing to a chat could affect recipients or unread state.

Mitigation: Treat message text as data, require explicit approval before each post, and do not write the consumptionhorizon read marker from a shell.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and Teams data excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires access to a signed-in Teams browser session to capture a bearer token.]

## Skill Version(s):

0.6.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
