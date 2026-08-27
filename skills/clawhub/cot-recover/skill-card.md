## Description:

Scan for orphaned worktrees and stale branches after crashes or abandoned sessions. Offers safe cleanup options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after crashes, abandoned agent sessions, or periodic repository hygiene checks to find orphaned Git worktrees, stale branches, and prunable Git state before deciding what to clean up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup actions can remove worktrees or delete branches if approved without careful review.

Mitigation: Review reported branch names, worktree paths, and commit hashes before approving any cleanup command.

Risk: Git worktree listings alone cannot prove whether a session is still active.

Mitigation: Classify uncertain recent worktrees as unknown activity and avoid cleanup unless additional evidence supports removal.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with Git command snippets and proposed cleanup actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only scan guidance by default; cleanup commands require explicit user approval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
