## Description:

OpenClaw Memory Distill organizes conversation context into local long-term memory and daily log files with first-run memory building, deduplication, sensitive-information skipping, archival safeguards, and per-agent isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to distill active conversations into structured local memory files so future sessions can recover durable decisions, tasks, preferences, and project context without preserving sensitive secrets by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill maintains local long-term memory from conversation history, which can preserve personal or sensitive context if not reviewed.

Mitigation: Review MEMORY.md and memory/ logs periodically, and expand sensitivePatterns to match the user's environment before relying on scheduled writes.

Risk: Cron-based memory distillation can write unattended conversation-derived summaries.

Mitigation: Enable cron only when unattended local memory updates are acceptable, and keep sensitive-information skipping enabled.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-memory-distill)
- [OpenClaw Memory Distill Documentation](https://github.com/dtsola/xiaoyaoclaw-memory-distill)
- [XiaoyaoClaw Guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [OpenClaw Workspace Initializer](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown summaries plus local Markdown memory files and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update MEMORY.md, memory/YYYY-MM-DD.md, and distill-config.json in the agent workspace after the appropriate confirmation or scheduled trigger.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
