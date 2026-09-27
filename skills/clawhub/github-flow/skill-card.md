## Description:

GitHub Flow guides agents through GitHub issue, pull request, review, merge, publishing, dependency, account-scope, and public-content sanitization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to convert plans and review findings into GitHub issues and pull requests, manage dependencies and publication flows, and perform gated review and merge operations with public-content sanitization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to operate GitHub with substantial authority, including issue and pull request mutations, branch publication, and merge workflows.

Mitigation: Install it only for agents authorized to operate the target repositories, require explicit user approval for publishing and merge actions, and review proposed GitHub CLI commands before execution.

Risk: The evidence security summary flags a helper pattern that can post pull request approvals from a second GitHub account.

Mitigation: Remove or disable alternate-account self-review helpers unless the organization explicitly permits that pattern and it cannot bypass required human-review protections.

Risk: Stored GitHub identities and token-scoped commands can misuse repository access if the active account or token scope is wrong.

Mitigation: Limit token scopes and accounts to the repositories needed, verify the active gh identity before operations, and prefer command-scoped token use for sensitive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Skill Overview](SKILL.md)
- [Changelog](CHANGELOG.md)
- [Authentication Scope Guide](auth-scope.md)
- [Pull Request Guide](pr.md)
- [Merge Guide](merge.md)
- [Public Content Sanitization Guide](sanitize.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and structured GitHub issue, pull request, review, and merge content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitHub CLI commands, checklist-style verification gates, and user-approval checkpoints for publishing or merge actions.]

## Skill Version(s):

0.11.2 (source: server release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
