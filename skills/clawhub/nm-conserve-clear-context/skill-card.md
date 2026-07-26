## Description: <br>
Manages context overflow by handing off to a fresh subagent at 80% usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to preserve task state and continue long-running work when context pressure reaches critical levels. It is intended for context handoffs that save a session checkpoint, delegate continuation to a fresh subagent, and resume work with documented state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Continuation agents may preserve unattended or dangerous execution modes and continue work without fresh user confirmation. <br>
Mitigation: Install only when automated context handoffs are intentional, and rely on runtime approval checks for destructive or public side effects. <br>
Risk: Session checkpoints may expose sensitive task context if used in repositories or sessions containing secrets, credentials, or sensitive business plans. <br>
Mitigation: Avoid using the skill on sensitive sessions unless the runtime and repository policies prevent secret capture and restrict access to checkpoint files. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-conserve-clear-context) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Source homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown with inline code blocks and checkpoint templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent handoff instructions, session-state templates, threshold guidance, and environment variable configuration notes.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
