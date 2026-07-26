## Description: <br>
Safe Exec 0.3.2 helps OpenClaw agents assess shell command risk, intercept dangerous operations, request user approval, and audit command activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucky-2968](https://clawhub.ai/user/lucky-2968) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to add a local approval and audit layer around shell commands issued by OpenClaw agents, especially commands that may delete data, modify system paths, or change privileged settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approval bypasses can allow risky commands to run without reliable human approval. <br>
Mitigation: Keep SafeExec enabled, avoid SAFE_EXEC_AUTO_CONFIRM and agent-driven approvals, and require explicit human review before approving pending requests. <br>
Risk: The skill wraps a local shell and can execute arbitrary commands. <br>
Mitigation: Install only in environments where a local shell wrapper is acceptable, review pending command text before approval, and inspect the local audit log for command history. <br>
Risk: Context text is not reliable proof of user consent. <br>
Mitigation: Do not rely on SAFEXEC_CONTEXT alone for approval; confirm high-risk operations through the pending request workflow. <br>
Risk: Included Git publishing tools and monitoring documents expand the review surface. <br>
Mitigation: Review the publishing tools and monitoring-related documentation before using those workflows. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/lucky-2968/skills/safe-exec-0-3-2) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [SafeExec issue tracker](https://github.com/OTTTTTO/safe-exec/issues) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and terminal text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local pending request records and audit log entries for reviewed command executions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; display/artifact release label Safe Exec 0.3.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
