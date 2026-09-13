## Description:

Automates code review workflows by obtaining repositories when needed, running multi-dimensional quality checks, and producing structured review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinycen](https://clawhub.ai/user/tinycen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review local or remote repositories, triage code quality issues, and generate Markdown reports for follow-up. It also supports scheduled reviews and explicit front-end/back-end integration review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may clone private repositories and use local credentials.

Mitigation: Run it in a disposable sandbox with least-privilege credentials and require explicit approval before SSH key, clone, or report transmission actions.

Risk: The skill may install and run project tooling from reviewed repositories.

Mitigation: Treat target repositories as untrusted input and approve dependency installation or tool execution only after reviewing the requested commands.

Risk: The skill may reset managed checkouts, write review files, and push commits.

Mitigation: Use dedicated working copies and require explicit approval before reset, commit, push, or other repository-modifying operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tinycen/skills/code-review)
- [Skill entrypoint](SKILL.md)
- [Manual review workflow](workflows/manual_workflow.md)
- [Scheduled review workflow](workflows/scheduled_workflow.md)
- [Cross-repository integration workflow](workflows/cross_repo_integration_workflow.md)
- [Repository access guidance](references/repository_access.md)
- [Review process and issue grading](references/review_process.md)
- [Report delivery guidance](references/report_delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, review summaries, file paths, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create review reports and ignored-issue lists under docs/code_reviews/ for the reviewed repository.]

## Skill Version(s):

1.3.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
