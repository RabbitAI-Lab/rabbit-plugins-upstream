## Description:

Session Recovery helps agents restore project context by maintaining STATUS.md, QUICK_RECOVERY.md, memory logs, and supporting scripts for status updates, daily notes, and weekly archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blqbzf](https://clawhub.ai/user/blqbzf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-assisted project teams use this skill to preserve working state across long-running or multi-task sessions. It provides project-local recovery files and commands for quickly rebuilding useful context after a new session starts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-local session summaries can capture sensitive project details in STATUS.md, QUICK_RECOVERY.md, and memory/.

Mitigation: Review generated memory files before committing or sharing them, and avoid writing secrets into summaries.

Risk: Weekly archiving can move or overwrite memory records.

Mitigation: Harden or avoid weekly_archive.sh until its archive behavior is fixed, and keep backups or version control for memory/.

## Reference(s):

- [Session Recovery Optimization](artifact/references/SESSION_RECOVERY_OPTIMIZATION.md)
- [Context Compression: Simple Explanation](artifact/references/上下文压缩_简单解释.md)
- [Context Compression: Original Text Preservation](artifact/references/上下文压缩_原文保存机制.md)
- [Context Compression: Information Loss and Recognition](artifact/references/上下文压缩_信息丢失与识别.md)
- [ClawHub Skill Page](https://clawhub.ai/blqbzf/skills/session-recovery)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and project-local file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local session memory artifacts such as STATUS.md, QUICK_RECOVERY.md, and memory/YYYY-MM-DD.md.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
