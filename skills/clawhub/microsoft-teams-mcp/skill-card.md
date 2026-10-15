## Description:

Guides agents to read Microsoft Teams chats, channels, unread messages, inline images, and activity from a signed-in browser session using shell helpers instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized Teams users can retrieve chats, channel messages, unread items, inline images, and the Activity feed from scripts without installing the Microsoft Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured Teams bearer token grants access to private chats and activity while valid.

Mitigation: Review before installing, use only with an authorized signed-in account, and remove ~/.teams-fpx/curlrc when token caching is no longer needed.

Risk: Untrusted extra curl arguments could send the cached token beyond the intended request scope.

Mitigation: Do not pass untrusted or model-generated extra curl arguments to the shell helpers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples; retrieved Teams responses may be JSON or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Teams guidance; excludes Calendar and shared-file downloads.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
