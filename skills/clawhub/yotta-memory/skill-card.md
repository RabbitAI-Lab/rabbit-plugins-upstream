## Description:

Provides persistent, file-based memory for AI agents, including cross-session recall, semantic search, and access controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to save and retrieve memories across sessions, search prior context, and maintain separate public and private memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory may retain sensitive information across sessions.

Mitigation: Avoid storing tokens or agent keys in memories; review what is saved and who can access it.

Risk: A locally running service can expose memories to other devices if LAN access is enabled or authentication is disabled.

Mitigation: Keep the service bound to localhost unless LAN access is intentional, and never use --no-auth on a reachable network.

Risk: Credential handling and expanded MCP tools can increase access to private memories and local actions.

Mitigation: Prefer key files or a secret store, use --tools core for an always-on MCP connection, and review provider, embedding, model, runtime, and LAN settings before enabling them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (publisher-provided)](https://github.com/YottaMeta/yotta-memory)
- [Memory protocol](references/protocol.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain text with optional command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recalled memory excerpts and cross-session context summaries.]

## Skill Version(s):

0.22.5 (source: ClawHub release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
