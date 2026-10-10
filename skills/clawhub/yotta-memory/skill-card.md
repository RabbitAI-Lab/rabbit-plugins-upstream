## Description:

Provides file-based, long-term memory for AI agents, with cross-session recall, semantic search, and access boundaries for private memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use this skill to retain and retrieve context between sessions, organize local memories, and share selected facts across agents while isolating private entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memories may retain personal information or credentials.

Mitigation: Review what is saved and avoid storing bearer tokens or agent keys in memory entries.

Risk: A LAN-facing memory service can expose stored information if authentication is disabled.

Mitigation: Prefer stdio or loopback-only access; never use --no-auth on a reachable network.

Risk: Autostart, scheduled backups, configuration changes, or optional provider commands may run or persist without the user's intent.

Mitigation: Review autostart, backup scheduling, MCP configuration edits, and provider, embedding, or distillation commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (not verified import provenance)](https://github.com/YottaMeta/yotta-memory)
- [Memory protocol](references/protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown memory entries and retrieved context in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent local memory; retrieved content depends on access permissions and stored entries.]

## Skill Version(s):

0.22.7 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
