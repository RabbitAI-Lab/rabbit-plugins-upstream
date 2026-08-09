## Description: <br>
Scan for orphaned worktrees and stale branches after crashes or abandoned sessions. Offers safe cleanup options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect git worktrees and branches after crashes, abandoned sessions, or periodic repository hygiene checks. It reports candidate stale state and proposes cleanup commands that require explicit approval before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup actions such as branch deletion, worktree removal, merge, cherry-pick, and remote prune can change or discard repository state. <br>
Mitigation: Review the generated report and approve only the specific cleanup actions you intend to run. <br>
Risk: A worktree with recent activity may be incorrectly treated as abandoned if session activity cannot be proven. <br>
Mitigation: Classify recent or uncertain worktrees as unknown activity and avoid cleanup unless the user confirms they are abandoned. <br>
Risk: Unmerged commits or uncommitted changes may be lost if cleanup is approved without preserving the work. <br>
Mitigation: Inspect status, branch, and recent commits first, then prefer merge or cherry-pick over discard when useful work exists. <br>


## Reference(s): <br>
- [Recover skill page](https://clawhub.ai/conorbronsdon/skills/recover) <br>
- [conorbronsdon publisher profile](https://clawhub.ai/user/conorbronsdon) <br>
- [agent-workspace canonical home](https://github.com/conorbronsdon/agent-workspace) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only scan by default; cleanup actions are presented for explicit user approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
