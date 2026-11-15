## Description:

Automates code quality reviews across GitHub and other repositories, then generates structured review reports for delivery in different workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinycen](https://clawhub.ai/user/tinycen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review local or remote repositories, check code quality across several languages, and produce structured Markdown reports. It can also compare explicitly paired frontend and backend repositories for interface consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review workflows may delete or move local files, including resetting changes or archiving reports.

Mitigation: Use disposable, uniquely identified sandbox checkouts without personal credentials, and require explicit authorization before destructive cleanup.

Risk: Review workflows may execute repository-controlled code or install external tools and project dependencies.

Mitigation: Keep review tools separate from development environments, use repository-scoped read-only access where possible, and verify downloaded installers before use.

Risk: Remote review workflows may commit or publish changes, configure access, or update project files.

Mitigation: Require explicit authorization for remote publication and configuration changes; use read-only repository access when write access is unnecessary.

## Reference(s):

- [Manual review workflow](workflows/manual_workflow.md)
- [Scheduled review workflow](workflows/scheduled_workflow.md)
- [Cross-repository review workflow](workflows/cross_repo_integration_workflow.md)
- [Review process and checks](references/review_process.md)
- [Repository access guidance](references/repository_access.md)
- [Report delivery guidance](references/report_delivery.md)
- [ClawHub skill page](https://clawhub.ai/tinycen/skills/code-review)
- [ModelScope release archive](https://modelscope.cn/skills/tinycen/code-review/archive/zip/master.zip)
- [Volta Node version manager](https://volta.sh)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown review reports and concise review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include issue severity, repository and commit details, report paths, and cross-repository consistency findings.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
