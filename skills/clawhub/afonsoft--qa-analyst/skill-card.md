## Description:

Use when the user asks for QA analysis, test planning, test cases, or root-cause analysis of a defect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and QA reviewers use this skill to analyze requirements, plan tests, create traceable test cases, execute QA checks, report defects, and perform root-cause analysis before release or pull request readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to inspect repository context and run normal QA commands, which may expose sensitive code, credentials, or production data in prompts or command output.

Mitigation: Use it in trusted repositories and review commands, logs, and scan output before sharing or publishing results.

Risk: The skill may write QA documentation or prepare GitHub issue content that includes defect details, evidence, branch names, or environment information.

Mitigation: Review generated documents and issue content before committing files or opening issues, especially for private projects or sensitive defects.

## Reference(s):

- [QA templates](references/qa-templates.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/qa-analyst)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Repository metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured QA reports, test plans, bug reports, verification summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portuguese user-facing clarification prompts; English internal documentation; may write QA documentation and propose GitHub issue content.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
