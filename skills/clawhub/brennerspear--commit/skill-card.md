## Description:

Create a git commit with a contextual message based on current changes, then push the branch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brennerspear](https://clawhub.ai/user/brennerspear)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to let an agent inspect repository changes, create one contextual Git commit, and push the current branch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically commit and push all repository changes, including unreviewed new files, secrets, and generated artifacts.

Mitigation: Before invoking the skill, manually inspect untracked files, secrets, generated artifacts, and the target remote and branch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/brennerspear/skills/commit)

## Skill Output:

**Output Type(s):** [Shell commands, Text]

**Output Format:** [Git operations executed through shell commands with a contextual commit message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stages repository changes, creates one commit, and pushes the current branch.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
