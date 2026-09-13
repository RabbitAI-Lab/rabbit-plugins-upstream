## Description:

Use when the user asks for QA analysis, test planning, test cases, or root-cause analysis of a defect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and product teams use this skill to analyze requirements, plan tests, create traceable test cases, execute verification, report defects, and perform root-cause analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-facing clarification and bug-report prompts may be in Portuguese, which can be unexpected for English-only teams.

Mitigation: Confirm language expectations before adoption and translate or adapt user-facing QA prompts where needed.

Risk: The skill may propose QA artifacts and project verification commands that affect workflow decisions.

Mitigation: Review generated plans, test cases, and commands in the target repository context before relying on them.

Risk: The skill may recommend opening GitHub issues for serious defects.

Mitigation: Require user approval and check the issue title, reproduction steps, evidence, severity, and priority before creating an issue.

## Reference(s):

- [QA templates](references/qa-templates.md)
- [Source repository metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured QA sections, templates, and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Portuguese user-facing clarification questions, QA artifact templates, verification reports, and issue-opening guidance.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
