## Description: <br>
Session Recovery helps agents and developers restore project context with status dashboards, quick-recovery notes, memory logs, and local scripts for recurring updates and archives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blqbzf](https://clawhub.ai/user/blqbzf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent users, and project teams use this skill to maintain local project memory, recover useful context across long-running sessions, and reduce repeated context loading with structured status and daily logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved project-memory notes can contain sensitive prompts, customer data, credentials, or confidential project details. <br>
Mitigation: Do not store secrets or confidential data in STATUS.md or memory files, and review summaries before relying on them as authoritative context. <br>
Risk: Optional automation such as local scripts, Git hooks, or Cron examples can update, archive, or stage project-memory files automatically. <br>
Mitigation: Review the scripts and generated file changes before enabling automation, archiving, or commit hooks in a project. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/blqbzf/session-recovery) <br>
- [README](README.md) <br>
- [Session Recovery Optimization](references/SESSION_RECOVERY_OPTIMIZATION.md) <br>
- [Context Compression Overview](references/上下文压缩_简单解释.md) <br>
- [Context Compression Original Text Handling](references/上下文压缩_原文保存机制.md) <br>
- [Context Compression Information Loss and Recognition](references/上下文压缩_信息丢失与识别.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and project-memory templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local STATUS.md, QUICK_RECOVERY.md, and memory/*.md files when users run the bundled scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
