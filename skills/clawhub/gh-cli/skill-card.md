## Description:

GitHub CLI for remote repository analysis, file fetching, codebase comparison, and discovering trending code/repos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to guide GitHub CLI workflows for analyzing repositories without cloning, comparing codebases, fetching files, searching GitHub, and managing common repository operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes GitHub CLI commands that can mutate repositories, issues, pull requests, workflows, releases, extensions, or local configuration.

Mitigation: Require explicit human approval before running state-changing commands, and prefer read-only analysis commands for routine repository inspection.

Risk: GitHub tokens may be over-scoped or exposed through token-display, auth, or credential-helper workflows.

Mitigation: Use read-only or narrowly scoped tokens where possible, avoid commands that print credentials, and review any credential-helper changes before execution.

Risk: Commands touching SSH, GPG, Codespaces, or credential configuration can change the user's local security posture.

Mitigation: Treat local authentication and configuration changes as privileged operations that require prior review and confirmation.

Risk: Some documented GitHub CLI preview commands and command fields may change across GitHub CLI versions.

Mitigation: Check behavior against the installed GitHub CLI version and the upstream manual, especially when using preview commands or scripted automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/gh-cli)
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/gh-cli)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub CLI repository](https://github.com/cli/cli)
- [GitHub search documentation](https://docs.github.com/en/search-github)
- [Remote repository analysis](references/remote-analysis.md)
- [Compare two codebases](references/comparison.md)
- [Discovering trending content](references/discovery.md)
- [GitHub CLI search](references/search.md)
- [Special syntax and command quirks](references/syntax.md)
- [GitHub operations reference](references/repositories.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitHub CLI environment variables such as GH_TOKEN, GITHUB_TOKEN, and GH_HOST.]

## Skill Version(s):

1.3.3 (source: frontmatter, changelog, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
