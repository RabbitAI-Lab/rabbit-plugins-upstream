## Description: <br>
Advanced git operations beyond add/commit/push. Use when rebasing, bisecting bugs, using worktrees for parallel development, recovering with reflog, managing subtrees/submodules, resolving merge conflicts, cherry-picking across branches, or working with monorepos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill for advanced Git workflows such as interactive rebase, bisect, worktrees, reflog recovery, cherry-pick, conflict resolution, sparse checkout, subtrees, and submodules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some examples use destructive Git commands such as hard resets, submodule cleanup, and stash clearing. <br>
Mitigation: Review git status, confirm the exact branch, ref, and path, and create a backup branch or stash before using destructive commands. <br>
Risk: Advanced Git recovery and history-editing guidance can affect shared history or local work if applied to the wrong repository state. <br>
Mitigation: Use the commands as reviewable guidance, avoid rebasing shared commits, and verify the intended repository state before running them. <br>


## Reference(s): <br>
- [Git Workflows on ClawHub](https://clawhub.ai/gitgoodordietrying/skills/git-workflows) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Git; examples should be reviewed against the active repository, branch, ref, and path before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
