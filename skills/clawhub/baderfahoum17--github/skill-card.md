## Description:

Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baderfahoum17](https://clawhub.ai/user/baderfahoum17)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to have an agent propose GitHub CLI commands for pull requests, issues, workflow runs, and GitHub API queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help prepare GitHub CLI commands that may read or change repository data depending on the user's authenticated `gh` scopes.

Mitigation: Review local GitHub CLI authentication scopes and confirm commands before running mutating operations, especially for private or organization repositories.

Risk: Advanced `gh api` and `--jq` usage can produce incomplete or misleading results if the repository, endpoint, or filter is wrong.

Mitigation: Check repository targets, API paths, and filters before acting on command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baderfahoum17/skills/github)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls]

**Output Format:** [Markdown guidance with inline shell command examples and JSON/JQ output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitHub CLI authentication and repository access appropriate to the requested GitHub operation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
