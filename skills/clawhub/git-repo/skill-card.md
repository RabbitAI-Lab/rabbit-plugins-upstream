## Description:

Helps developers manage Git repositories and worktrees, troubleshoot hooks, and configure SourceGit and multi-account access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect, repair, and reorganize Git repositories and worktrees, manage account-specific credentials, and diagnose hook or merge problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some worktree cleanup and repository conversion workflows can delete worktrees or overwrite uncommitted changes.

Mitigation: Inspect repository status and active operations, preserve uncommitted work, and review any destructive action before proceeding.

Risk: The repo-to-ghq and local-to-staging-pr workflows may mishandle cleanup or index rebuilding on dirty repositories.

Mitigation: Avoid these workflows when uncommitted work or active Git operations exist until their behavior is fixed or manually audited.

Risk: Credential and SourceGit configuration changes can affect which account or repository is used.

Mitigation: Review proposed configuration changes and confirm the intended account and repository before applying them.

## Reference(s):

- [Git Repo on ClawHub](https://clawhub.ai/drumrobot/skills/git-repo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to Git metadata, worktrees, credentials, and SourceGit preferences.]

## Skill Version(s):

0.12.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
