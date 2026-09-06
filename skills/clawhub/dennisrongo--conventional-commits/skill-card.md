## Description:

Write git commit messages following the Conventional Commits specification, with an automatic ticket number pulled from the current branch and a project tag (API / CLIENT / CONSOLE / DB) when the project type can be detected from the diff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft Conventional Commits messages from the current branch and Git diff, including ticket and project context when those signals are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local branch names and staged or unstaged Git diffs, which may expose sensitive uncommitted code or secrets to the agent during commit-message drafting.

Mitigation: Use it only in repositories where sharing current branch and diff context with the agent is acceptable, and avoid invoking it when uncommitted changes contain secrets or highly sensitive material.

Risk: Generated commit messages can misrepresent the change if the diff spans unrelated work or the inferred project tag does not fit the repository.

Mitigation: Review the proposed message before committing and split unrelated changes into separate commits when the skill flags mixed changes.

## Reference(s):

- [Conventional Commits specification](https://www.conventionalcommits.org/)
- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/conventional-commits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text commit message with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commit message headers are constrained by the skill to Conventional Commits syntax and a 72-character header budget.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
