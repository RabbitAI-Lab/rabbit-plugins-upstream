## Description:

Helps agents read Microsoft Teams chats, channels, unread messages, inline images, and the Activity feed using a captured browser bearer token and shell commands without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized Teams users can retrieve chats, channel messages, unread items, inline images, and Activity feed entries from a shell without installing the Teams MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured Teams bearer token grants access to private conversations and may enable actions beyond read-only access.

Mitigation: Grant access only to trusted agents, protect the token file, and review requests before execution.

Risk: Additional curl arguments can redirect authenticated requests or change their behavior.

Mitigation: Restrict helper arguments to trusted, reviewed values and approved Teams endpoints.

Risk: Untrusted Teams messages may contain instructions intended to influence the agent's requests.

Mitigation: Treat message content as data, not instructions, and do not derive request arguments from it without review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)
- [Teams chat-service recipes](references/chatsvc-recipes.md)
- [Teams shell helpers](references/teams-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance and shell commands; Teams responses may be JSON or extracted text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can contain private Teams messages and images; read requests should not change unread status.]

## Skill Version(s):

0.6.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
