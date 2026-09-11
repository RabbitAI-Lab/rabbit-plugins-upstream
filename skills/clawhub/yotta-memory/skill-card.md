## Description:

元忆 yotta-memory gives AI agents a boundary-aware, file-based memory workflow for storing, recalling, auditing, and rolling back persistent memories across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give AI agents persistent local memory with explicit public/private boundaries, recall workflows, lifecycle maintenance, and optional MCP access across sessions or machines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool gives agents broad persistent and remote access to private memories, and ClawHub security evidence reports verified owner-isolation gaps.

Mitigation: Review before installation, avoid sharing one memory store across untrusted agents until owner-scoped MCP authorization fixes are available, and keep private memories limited to trusted identities.

Risk: LAN or MCP exposure can make memory access reachable beyond the local machine.

Mitigation: Keep services bound to localhost unless the network is trusted, avoid --no-auth, and use separate revocable tokens for each agent.

Risk: Persistent memory operations, import/export, and maintenance commands can expose or alter user memory data.

Mitigation: Do not store MCP tokens in memory entries, keep backups before maintenance/import/export, and review memory changes before applying destructive or bulk operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [README](artifact/README.md)
- [User Guide](artifact/USER_GUIDE.md)
- [Protocol Reference](artifact/references/protocol.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with CLI commands, MCP configuration snippets, and generated local memory files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can cause agents to create or modify persistent local memory stores when users approve the workflow.]

## Skill Version(s):

0.11.1 (source: ClawHub release metadata; artifact files report 0.11.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
