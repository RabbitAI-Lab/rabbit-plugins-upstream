## Description:

Automates repository code review by cloning or using local projects, running multi-dimensional quality checks, and producing structured Markdown review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinycen](https://clawhub.ai/user/tinycen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review local or remote repositories for code quality, security, maintainability, dependency, and cross-repository integration issues. It is suited for manual reviews, scheduled checks, and frontend/backend integration review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run package managers and install dependencies while preparing review environments.

Mitigation: Use disposable clones or containers, prefer isolated environments, avoid automatic dependency scripts, and record degraded checks when installation fails.

Risk: The skill can create or use SSH authentication and push review artifacts to a remote repository.

Mitigation: Use read-only or least-privilege credentials where possible and require explicit confirmation before SSH key creation, git commit, or git push.

Risk: The skill documentation includes destructive repository update steps such as git reset and git clean.

Mitigation: Run reviews in disposable clones or confirm before destructive git operations, especially when a local working tree may contain user changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tinycen/skills/code-review)
- [Repository Access](references/repository_access.md)
- [Review Process](references/review_process.md)
- [Report Delivery](references/report_delivery.md)
- [Cross-Repository Integration Checks](references/cross_repo_integration_checks.md)
- [Python Review Tool Dependencies](references/python_dependency_installation/review_tools.md)
- [Frontend Node Environment](references/frontend_dependency_installation/node_environment.md)
- [Volta](https://volta.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown review reports with summary text, issue lists, code snippets, and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create review report files and ignored-issue tracking files under docs/code_reviews/.]

## Skill Version(s):

1.3.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
