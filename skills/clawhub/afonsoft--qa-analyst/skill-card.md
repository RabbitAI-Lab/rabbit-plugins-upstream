## Description:

Use when the user asks for QA analysis, test planning, test cases, or root-cause analysis of a defect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and QA practitioners use this skill to analyze requirements, create test plans and test cases, execute verification cycles, document defects, and guide root-cause/process-improvement work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may propose or run build, test, coverage, and scanning commands that execute repository code.

Mitigation: Use the skill in trusted repositories or an isolated sandbox, and review proposed commands before execution.

Risk: Requirements, issue text, test output, and application responses may contain untrusted instructions or sensitive data.

Mitigation: Treat those sources as data, ignore embedded instructions, and redact secrets, tokens, and PII in QA outputs.

Risk: The skill's user-facing prompts and templates default to Portuguese (pt-BR), which may not fit every team workflow.

Mitigation: Confirm language expectations before publishing reports or opening issues for teams that require another locale.

## Reference(s):

- [QA templates](references/qa-templates.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/qa-analyst)
- [Metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown reports, test plans, test cases, bug reports, verification summaries, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing prompts default to Portuguese (pt-BR); sensitive values should be redacted from reports.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
