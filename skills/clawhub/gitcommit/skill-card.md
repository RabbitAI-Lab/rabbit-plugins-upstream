## Description:

Use when the user explicitly asks to prepare, review, or create a Git commit, including "提交", "提交代码", "帮我提交", "commit", "git commit", "确认提交", or requests a commit message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlykan](https://clawhub.ai/user/wlykan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect repository changes, group them by business intent, draft Conventional Commit messages, and execute commits only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed commit plan could group unrelated changes or use a misleading commit message.

Mitigation: Review the generated file groups, rationale, and commit messages before giving explicit confirmation.

Risk: Sensitive files, binary files, or mixed staged and unstaged changes may be present in the worktree.

Mitigation: Confirm exclusions, large or binary file handling, and mixed-state files before allowing the skill to stage or commit anything.

Risk: Repository state can change between plan review and execution.

Mitigation: The skill rechecks repository status and invalidates the prior confirmation if paths, content, staged state, or rules changed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlykan/skills/gitcommit)
- [Publisher profile](https://clawhub.ai/user/wlykan)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown plan with commit messages, file groupings, risk notes, and optional execution results after confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Git status summaries, changed-path coverage counts, commit hashes, and remaining worktree state; secret values are not exposed.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
