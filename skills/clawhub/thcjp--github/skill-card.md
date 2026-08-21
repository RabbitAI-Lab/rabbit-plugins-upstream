## Description:

GitHub开发工具 helps agents use the GitHub CLI to manage repositories, issues, pull requests, workflow runs, and GitHub API calls with Chinese interaction support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to delegate explicit GitHub repository-management tasks to an agent through the gh CLI, including issue, pull request, workflow-run, and API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use authenticated GitHub authority through gh and may perform broad repository-management operations.

Mitigation: Keep use to explicit GitHub tasks, review proposed commands before execution, and prefer a least-privileged GitHub token or account.

Risk: Private repository data, tokens, or other sensitive information could be exposed in prompts, command output, or logs.

Mitigation: Avoid sharing tokens or private repository data in logs, redact sensitive output, and verify that generated commands do not print secrets.

Risk: The security summary flags vague scope and weak safety guarantees for command and repository-management powers.

Mitigation: Use the skill in a sandboxed or reviewed workflow and scan/review changes before relying on them in production repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute authenticated gh CLI operations that can affect repositories, issues, pull requests, workflow runs, and API resources.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
