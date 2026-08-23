## Description:

Automates repository code review workflows by cloning or using local code, running quality checks, and producing structured Markdown review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinycen](https://clawhub.ai/user/tinycen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review local or remote repositories, check Python and JavaScript project quality, and generate Markdown reports with findings, ignored issues, and cross-repo integration notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository cleanup, report commits, and pushes can change or publish files in the target repository.

Mitigation: Use disposable clones or read-only access where possible, and require manual confirmation before any git push, reset, clean, or file mutation.

Risk: SSH key setup can alter local authentication state and expose a public key for account configuration.

Mitigation: Require explicit user confirmation before generating or reusing SSH keys, and limit use to repositories where that access path is intended.

Risk: Dependency installation during review can run package manager logic from the target project.

Mitigation: Prefer isolated environments, inspect dependency files first, and require confirmation before installing project dependencies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tinycen/skills/code-review)
- [Skill entrypoint](SKILL.md)
- [Manual review workflow](workflows/manual_workflow.md)
- [Scheduled review workflow](workflows/scheduled_workflow.md)
- [Cross-repo integration workflow](workflows/cross_repo_integration_workflow.md)
- [Repository access](references/repository_access.md)
- [Review process](references/review_process.md)
- [Report delivery](references/report_delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create report files under docs/code_reviews/ and update ignored_issues.md when used in a writable repository.]

## Skill Version(s):

1.3.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
