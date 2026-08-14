## Description:

精英长记忆 provides a long-term memory workflow for AI agents using WAL-style state updates, hybrid retrieval, tiered storage, cost controls, and memory hygiene across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to configure persistent memory across sessions, retrieve prior decisions and preferences, and manage memory cost, hygiene, and storage layers for AI agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain conversation details locally or in external memory services across broad agent-use scenarios.

Mitigation: Decide which storage layers are allowed before use, keep Mem0 and SuperMemory disabled unless external services are explicitly approved, and avoid storing secrets or regulated data.

Risk: Long-term memory files, daily logs, vector stores, Git notes, and backups can accumulate sensitive or stale context.

Mitigation: Periodically review, delete, or prune SESSION-STATE.md, MEMORY.md, daily logs, vector stores, Git notes, and exported backups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/longmemo-elite)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to create or update memory files, vector stores, Git notes, exported backups, and optional external memory-service records.]

## Skill Version(s):

1.0.3 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
