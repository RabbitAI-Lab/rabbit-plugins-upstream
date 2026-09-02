## Description:

Recovers broken agent state via crash recovery, context overflow, and merge conflict protocols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to recover from interrupted agent sessions, context loss, merge conflicts, and mismatches between task state, git state, and on-disk artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words may surface the skill during general discussions of context or state.

Mitigation: Confirm that the current task is actually crash recovery, context overflow, merge conflict resolution, or state reconciliation before following the playbook.

Risk: Recovery procedures may suggest git stash, commit, abort, reset, or file-restore actions that affect the worktree.

Mitigation: Review the current git status, diffs, and command intent before allowing any worktree-modifying action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-damage-control)
- [Publisher profile](https://clawhub.ai/user/athola)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell command examples and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces recovery procedures and decision criteria; it does not include executable scripts or installers.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
