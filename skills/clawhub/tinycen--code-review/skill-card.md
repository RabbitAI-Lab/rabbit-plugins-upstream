## Description:

Automates code quality review by cloning or using local repositories, running multi-dimensional checks, and producing structured review reports for manual, scheduled, and cross-repository frontend/backend scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinycen](https://clawhub.ai/user/tinycen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review local or remote repositories, identify code quality and integration issues, and produce Markdown reports with issue severity and remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can clone repositories, install or upgrade analysis tools, and write review artifacts.

Mitigation: Run it in a disposable workspace or fresh clone and review generated files before adopting changes.

Risk: Remote and scheduled modes can commit and push docs/code_reviews artifacts or ignored issue state.

Mitigation: Review generated commits before pushing and limit credentials to repositories where report publication is intended.

Risk: Repository update workflows can discard local changes.

Mitigation: Avoid running it on important dirty working trees; commit or stash local work first.

Risk: SSH key generation and clone proxy fallbacks may affect repository access posture.

Mitigation: Use preconfigured least-privilege SSH keys and approve proxy fallback only when acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tinycen/skills/code-review)
- [Repository access](references/repository_access.md)
- [Review process](references/review_process.md)
- [Report delivery](references/report_delivery.md)
- [Cross-repository integration checks](references/cross_repo_integration_checks.md)
- [Manual review workflow](workflows/manual_workflow.md)
- [Scheduled review workflow](workflows/scheduled_workflow.md)
- [Cross-repository integration workflow](workflows/cross_repo_integration_workflow.md)
- [Single-repository report template](references/templates/report.md)
- [Cross-repository report template](references/templates/cross_repo_report.md)
- [Ignored issues template](references/templates/ignored_issues_template.md)
- [Python review tools](references/python_dependency_installation/review_tools.md)
- [Frontend Node environment](references/frontend_dependency_installation/node_environment.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and conversational guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create docs/code_reviews reports and ignored_issues.md in reviewed repositories; remote modes may propose commits or pushes for report artifacts.]

## Skill Version(s):

1.3.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
