## Description:

GitHub Flow helps agents convert plans, research, and implementation results into GitHub issues and pull requests while following documented review, auth, merge, dependency, and publication workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to prepare GitHub issue bodies, PR bodies, review comments, dependency links, branch publication steps, and merge workflows. It is most relevant when operating on GitHub repositories with the gh CLI and when repository changes need explicit test plans and public-facing sanitization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through broad GitHub write, review, dependency, branch, and merge operations.

Mitigation: Require explicit user confirmation before any GitHub write, merge, reviewer registration, dependency mutation, or branch cleanup.

Risk: GitHub CLI operations may run under the wrong account or token if local authentication state is stale.

Mitigation: Verify the active gh account, repository owner, and commit author identity before push, PR, review, or merge actions.

Risk: Issue bodies, PR bodies, and comments can accidentally expose internal paths or personal data in public repositories.

Mitigation: Apply the documented public-repository sanitization checks before posting any generated or edited public GitHub text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Skill overview](artifact/SKILL.md)
- [Auth scope guide](artifact/auth-scope.md)
- [PR guide](artifact/pr.md)
- [Merge guide](artifact/merge.md)
- [Sanitize guide](artifact/sanitize.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with GitHub CLI command examples, checklists, and workflow rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in GitHub issue, pull request, review, dependency, branch, and merge operations when an agent follows the guidance.]

## Skill Version(s):

0.9.1 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
