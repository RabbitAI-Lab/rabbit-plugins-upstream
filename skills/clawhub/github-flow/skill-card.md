## Description:

GitHub issue and pull request workflow automation for agents working with GitHub repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to turn plans, research, and implementation results into GitHub issues, pull requests, reviews, dependency links, and merge workflows. It is most useful when an agent needs structured GitHub CLI-based workflow guidance with verification plans and publication hygiene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through broad repository-mutating GitHub operations such as issue creation, PR body edits, review posting, pushes, and merges.

Mitigation: Install it only for trusted agents and review GitHub token scopes, account mappings, and confirmation behavior before use.

Risk: The skill sometimes tells the agent to proceed from inferred context, which can lead to unintended repository changes if the context is stale or wrong.

Mitigation: Require explicit confirmation for sensitive actions and verify repository, branch, account, and permission state through the GitHub CLI before mutation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)
- [auth-scope.md](auth-scope.md)
- [identity-auth.md](identity-auth.md)
- [pr.md](pr.md)
- [merge.md](merge.md)
- [sanitize.md](sanitize.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and structured GitHub workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to call the GitHub CLI and update GitHub issues, pull requests, reviews, branches, and merge state.]

## Skill Version(s):

0.8.2 (source: ClawHub release metadata and CHANGELOG, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
