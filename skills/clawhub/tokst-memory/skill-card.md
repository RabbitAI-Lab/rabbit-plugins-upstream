## Description:

Persistent memory for AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give AI agents durable TokST memory across sessions, projects, machines, and teams. It guides agents to load prior context, search decisions, and store facts, decisions, preferences, tasks, notes, architecture records, and file-backed memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may store broad user and project context in durable cloud or shared memory without asking before each write.

Mitigation: Use local SQLite mode when cloud sync is inappropriate, avoid storing secrets or regulated data, and review saved memories and attachments regularly.

Risk: Automatic memory writes and permanent delete workflows can preserve outdated context or remove useful records.

Mitigation: Search before storing, use source and tag conventions, archive stale memory before deletion when possible, and review what has been saved.

## Reference(s):

- [TokST documentation](https://tokst.com/docs)
- [TokST self-contained skill guide](https://tokst.com/skill.md)
- [TokST remote MCP endpoint](https://api.tokst.com/mcp)
- [ClawHub skill page](https://clawhub.ai/anthemty/skills/tokst-memory)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to read and write durable memory through TokST CLI and MCP workflows.]

## Skill Version(s):

0.6.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
