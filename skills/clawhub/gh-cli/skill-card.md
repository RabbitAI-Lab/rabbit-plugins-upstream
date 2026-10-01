## Description:

GitHub CLI for remote repository analysis, file fetching, codebase comparison, and discovering trending code/repos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to guide GitHub CLI workflows for repository analysis, file retrieval, codebase comparison, search, pull requests, issues, actions, and releases without cloning repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes guidance for broad GitHub CLI operations, including write, admin, token, extension, and codespace commands.

Mitigation: Use least-privilege GitHub tokens, prefer read-only scopes for analysis, and require explicit approval before executing mutating or administrative commands.

Risk: Commands that inspect authentication state, secrets, or token-backed resources can expose sensitive access details.

Mitigation: Avoid printing tokens or secrets, redact command output before sharing, and review any command that manages credentials, secrets, or keys before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/gh-cli)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/gh-cli)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub CLI repository](https://github.com/cli/cli)
- [GitHub search documentation](https://docs.github.com/en/search-github)
- [Remote repository analysis](references/remote-analysis.md)
- [Compare two codebases](references/comparison.md)
- [Discovering trending content](references/discovery.md)
- [Search reference](references/search.md)
- [Special syntax and command quirks](references/syntax.md)
- [Repositories reference](references/repositories.md)
- [Pull requests reference](references/pull_requests.md)
- [Issues reference](references/issues.md)
- [Actions reference](references/actions.md)
- [Releases reference](references/releases.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include GitHub CLI commands that require authentication and repository-specific review before execution.]

## Skill Version(s):

1.4.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
