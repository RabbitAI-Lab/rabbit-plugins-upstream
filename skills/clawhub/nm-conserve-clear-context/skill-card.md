## Description: <br>
Manages context overflow by handing off to a fresh subagent at 80% usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to preserve task state when an agent approaches context limits, then continue work through a fresh continuation subagent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist project state into .claude/session-state.md or a configured session-state path. <br>
Mitigation: Treat session-state files as sensitive, keep secrets out of them, and remove them when the handoff is no longer needed. <br>
Risk: The skill can carry unattended, no-confirmation, or dangerous execution modes into continuation agents. <br>
Mitigation: Use it with those modes only when remaining tasks are tightly scoped and preapproved. <br>
Risk: Continuation agents may proceed from incomplete or stale handoff context. <br>
Mitigation: Review the checkpoint before handoff, include active files and pending task IDs, and stop when human judgment is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-clear-context) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with session-state templates, inline code blocks, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a project-scoped session-state Markdown file for continuation handoff.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
