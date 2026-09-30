## Description:

Provides file-based, persistent memory for AI agents, including cross-session context recovery, semantic recall, and access boundaries between shared and private memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retain and retrieve task context across sessions, maintain local memory records, and separate shared facts from agent-private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote access tokens or agent keys could be retained in long-term memory.

Mitigation: Keep credentials in the MCP host configuration, OS keychain, password manager, or protected key file, not memory entries.

Risk: Installation or setup can change agent and MCP configuration.

Mitigation: Review proposed configuration edits before applying them.

Risk: Unauthenticated remote access or LAN autostart can expose a persistent memory service.

Mitigation: Avoid --no-auth except on a trusted isolated network; enable LAN autostart only when its persistent behavior is understood.

Risk: Configured extension providers can run local commands.

Mitigation: Review provider.json commands and enable only providers whose persistent execution you understand.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-memory)
- [Memory protocol](artifact/references/protocol.md)
- [Extension provider protocol](artifact/references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Plain text or JSON context and recall results; Markdown memory records and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores local, persistent memories with shared and agent-private scopes; supports review and rollback.]

## Skill Version(s):

0.19.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
