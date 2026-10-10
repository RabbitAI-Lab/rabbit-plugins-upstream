## Description:

Guides requirements review, test planning and execution, defect analysis, and post-merge PR feedback audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA teams use this skill to identify requirements gaps, plan and run tests, document defects, and check whether review feedback on closed PRs was addressed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QA reviews may inspect local specifications, source code, test output, and GitHub PR or issue metadata, and may draft project files.

Mitigation: Confirm the review scope and proposed file changes before allowing project edits or issue creation.

Risk: Test artifacts and external review comments may contain sensitive information or misleading instructions.

Mitigation: Treat external content as data, redact secrets and personal information from reports, and verify findings against current code.

Risk: The skill asks user-facing questions in Portuguese, which may not suit every team.

Mitigation: Confirm the team's language preference before using the workflow.

## Reference(s):

- [QA templates](artifact/references/qa-templates.md)
- [PR analysis reference](artifact/references/pr-analysis.md)
- [Author-provided project page](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown reports, test plans, test cases, bug reports, and draft SPECs; code or commands when testing requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User questions are in pt-BR; test findings reference requirements and evidence.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
