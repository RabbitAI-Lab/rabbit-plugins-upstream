## Description: <br>
Recovers broken agent state via crash recovery, context overflow, and merge conflict protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to recover interrupted or inconsistent agent sessions, including crashes, context overflow, merge conflicts, and divergent task, git, or disk state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recovery procedures may suggest git commits, stashes, staged-state resets, merge aborts, and task-list edits. <br>
Mitigation: Review each proposed recovery command before running it and record stash references, rollback choices, and recovery notes. <br>
Risk: Working in an uncertain agent session or worktree can obscure partial work or cause the wrong state to be treated as authoritative. <br>
Mitigation: Snapshot git status, diffs, recent history, and task state before applying rollback, conflict-resolution, or reconciliation actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-damage-control) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with inline shell command blocks and checklist templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recovery workflows cover crash recovery, context overflow, merge conflicts, state reconciliation, and risk assessment.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
