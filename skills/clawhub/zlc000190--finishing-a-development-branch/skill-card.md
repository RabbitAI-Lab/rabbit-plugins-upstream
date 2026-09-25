## Description:

Guides completion of development work by verifying tests, presenting structured integration choices, and handling merge, pull request, branch preservation, or discard workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zlc000190](https://clawhub.ai/user/zlc000190)

### License/Terms of Use:


## Use Case:

Developers and engineering agents use this skill after implementation is complete and tests pass to choose and execute a branch-finishing path. It supports local merge, pull request creation, branch preservation, or confirmed discard while emphasizing test verification and explicit user choice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting cleanup guidance could remove a local worktree after pull request creation when the user expected it to be preserved.

Mitigation: Before removing any worktree, verify the exact path and branch with the user and avoid cleanup after pull request creation unless the user explicitly confirms it.

Risk: Branch discard can permanently delete commits and local work.

Mitigation: Require the documented typed discard confirmation and show the branch, commit list, and worktree path before deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zlc000190/skills/finishing-a-development-branch)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with option prompts and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single conversational workflow for completing a development branch.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
