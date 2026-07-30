## Description: <br>
Optimizes context windows via MECW principles and memory tiering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill during long, multi-file, or tool-heavy tasks to assess context pressure, apply MECW guidance, coordinate subagent workflows, and keep working memory concise. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checkpoint, log, or coordination-file examples can expose secrets or sensitive conversation details if copied into shared or poorly cleaned storage. <br>
Mitigation: Avoid writing secrets or sensitive details to temporary files, logs, or coordination files; control permissions and cleanup when persistence is needed. <br>
Risk: Context-saving recommendations can omit useful detail if applied mechanically to tasks that require full evidence review. <br>
Mitigation: Use selective reads and summaries for triage, then inspect the underlying artifacts before final decisions or high-impact changes. <br>


## Reference(s): <br>
- [Context Optimization on ClawHub](https://clawhub.ai/athola/skills/nm-conserve-context-optimization) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only context management guidance; security evidence reports no hidden execution, exfiltration, or destructive behavior.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
