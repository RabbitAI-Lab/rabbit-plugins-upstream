## Description:

AI大脑学习记忆方法论 guides agents in organizing learning and long-term memory with layered memory types, encoding-storage-retrieval routines, review cycles, and memory-safety practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users use this skill to decide what an AI agent should remember, where to store it, how to retrieve it, and when to review or prune persistent memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages broad long-term memory management, including reading and changing persistent memory.

Mitigation: Confirm the exact memory files the agent may read or write before use, require approval before persistent changes, and keep a rollback path for memory edits.

Risk: Scheduled or automatic memory maintenance can alter retained context without enough user-control detail.

Mitigation: Use scheduled review or consolidation only in trusted scopes, and require human review before pruning, isolating, or rewriting important memory entries.

Risk: Persistent memory can preserve poisoned, stale, or sensitive information across future sessions.

Mitigation: Treat retrieved memory as untrusted input for important decisions, preserve provenance for memory entries, avoid storing secrets, and audit suspicious entries before reuse.

## Reference(s):

- [Research Sources and Evidence](references/调研出处与证据.md)
- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-brain-learning-memory)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional Python evaluation output as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled evaluation script uses synthetic data in a temporary directory and can emit a JSON results file.]

## Skill Version(s):

2.3.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
