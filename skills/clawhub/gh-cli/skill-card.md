## Description:

GitHub CLI for remote repository analysis, file fetching, codebase comparison, and discovering trending code/repos. Use when analyzing repos without cloning, comparing codebases, or searching for popular GitHub projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to ask an agent for GitHub CLI workflows that analyze repositories remotely, compare codebases, fetch files, search GitHub content, and work with common GitHub resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents broad GitHub account, repository, CI, credential, secret, release, issue, project, and pull request operations, including commands that can change remote state.

Mitigation: Use a least-privilege GitHub token and require explicit confirmation before running any command that changes GitHub state, credentials, secrets, keys, extensions, Codespaces, workflows, releases, issues, projects, or pull requests.

Risk: GitHub tokens or credential-related output may be exposed when commands are copied, logged, or summarized.

Mitigation: Avoid printing token values, redact sensitive command output, and prefer scoped environment variables such as GH_TOKEN only for the session that needs them.

Risk: Commands may target the wrong repository when gh infers context from the current working directory.

Mitigation: Pass --repo OWNER/REPO in scripted or agent-driven workflows so repository operations are directed at the intended target.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/gh-cli)
- [Skill source homepage](https://github.com/tenequm/skills/tree/main/skills/gh-cli)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub CLI repository](https://github.com/cli/cli)
- [GitHub Search documentation](https://docs.github.com/en/search-github)
- [Remote analysis reference](references/remote-analysis.md)
- [Codebase comparison reference](references/comparison.md)
- [Discovery reference](references/discovery.md)
- [Search reference](references/search.md)
- [Syntax reference](references/syntax.md)
- [Repository operations reference](references/repositories.md)
- [Pull request workflows reference](references/pull_requests.md)
- [Issue workflows reference](references/issues.md)
- [GitHub Actions reference](references/actions.md)
- [Release workflows reference](references/releases.md)
- [Setup and authentication reference](references/getting_started.md)
- [Extension reference](references/extensions.md)
- [Additional GitHub CLI reference](references/other.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitHub CLI commands that require gh, GitHub authentication, and an explicitly selected repository.]

## Skill Version(s):

1.3.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
