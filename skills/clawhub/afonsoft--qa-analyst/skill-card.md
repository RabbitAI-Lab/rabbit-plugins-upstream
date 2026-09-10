## Description:

Use when the user asks for QA analysis, requirement review, test planning, test cases, bug reports, root-cause analysis of defects, or mentions QA, quality assurance, testar essa feature, or revisar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to review requirements, plan tests, write traceable test cases, execute manual or automated verification, report defects, and analyze process gaps. User-facing clarifications are expected in Portuguese (pt-BR).

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect project specifications, context files, and existing test assets during QA analysis.

Mitigation: Run it only in the intended workspace and review the files it plans to inspect when sensitive project context is present.

Risk: The skill may run existing test suites or suggest local QA and issue-tracking commands.

Mitigation: Review commands before execution and keep GitHub issue creation, test additions, and other project changes under explicit user control.

## Reference(s):

- [QA templates](references/qa-templates.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/qa-analyst)
- [Metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with structured QA plans, test cases, bug reports, RCA notes, and inline commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Portuguese user-facing questions and English internal QA documentation.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
