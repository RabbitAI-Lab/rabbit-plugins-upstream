## Description: <br>
Compress OpenClaw session context safely with backups and restore steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanbastias](https://clawhub.ai/user/juanbastias) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to compress long session context while preserving the active task, current decisions, blockers, backups, and restore path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Context compression can omit useful decisions or promote weak summaries into durable memory or project guidance files. <br>
Mitigation: Use the skill only when context is genuinely too large, keep a backup and restore path, and review proposed memory or guidance-file changes before accepting them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juanbastias/skills/session-context-maintainer) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code; users review proposed context summaries and any memory or guidance-file updates before relying on them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
