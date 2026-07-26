## Description: <br>
GitHub CLI for remote repository analysis, file fetching, codebase comparison, and discovering trending code/repos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect GitHub repositories remotely, compare codebases, fetch files, search code, and discover repository patterns without cloning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents GitHub CLI operations that can expose tokens or change and delete GitHub resources. <br>
Mitigation: Use a narrowly scoped or read-only GitHub token where possible, and approve mutating, token-printing, extension, workflow, release, or deletion commands only when the user explicitly requested that action. <br>
Risk: Repository inference from the current working directory can silently target the wrong repository in scripted agent workflows. <br>
Mitigation: Pass --repo OWNER/REPO for GitHub CLI commands in agent or CI workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/gh-cli) <br>
- [Publisher Profile](https://clawhub.ai/user/tenequm) <br>
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/gh-cli) <br>
- [Official GitHub CLI Manual](https://cli.github.com/manual/) <br>
- [GitHub CLI Repository](https://github.com/cli/cli) <br>
- [GitHub Search Documentation](https://docs.github.com/en/search-github) <br>
- [Remote Repository Analysis](references/remote-analysis.md) <br>
- [Compare Two Codebases](references/comparison.md) <br>
- [Discovering Trending Content](references/discovery.md) <br>
- [Special Syntax & Command Quirks](references/syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the GitHub CLI binary and optionally GH_TOKEN, GITHUB_TOKEN, or GH_HOST environment variables.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
