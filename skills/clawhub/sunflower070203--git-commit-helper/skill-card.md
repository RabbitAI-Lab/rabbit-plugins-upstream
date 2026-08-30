## Description:

Analyze the current git changes, generate a Conventional Commits message, confirm with the user, then commit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunflower070203](https://clawhub.ai/user/sunflower070203)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect repository changes, draft a Conventional Commits message, confirm the intended scope and message, and create a git commit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can stage and commit repository changes, including all changes when the user chooses the full scope.

Mitigation: Review the displayed git status block and confirmed scope before approval, and exclude any files that should not be committed.

Risk: A generated commit message may not match the repository's intent or local convention.

Mitigation: Review and edit the proposed message before approval; the workflow requires explicit confirmation before committing.

Risk: Merge conflicts or unusual repository states can make a commit unsafe or misleading.

Mitigation: Pause when merge-in-progress is reported and decide how to proceed before generating or applying a commit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunflower070203/skills/git-commit-helper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline PowerShell and git command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a fixed-format git change analysis, a proposed commit scope, a proposed Conventional Commits message, and commit verification output.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
