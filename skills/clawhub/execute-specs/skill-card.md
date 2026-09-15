## Description:

Use when the user asks to implement an approved SPEC SDD using test-driven development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement an approved SPEC SDD with a strict red-green-refactor loop. It maps each test to a numbered requirement or acceptance criterion, validates each slice, and prepares the work for mandatory QA review before a pull request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill edits code and tests and runs validation commands while implementing an approved SPEC.

Mitigation: Install it only for repositories where agents are allowed to perform implementation work, and review the final diff, test results, and QA output before opening a pull request.

Risk: The workflow proceeds from one approved slice to the next without repeated approval prompts.

Mitigation: Use only approved SPEC files and ensure the SPEC accurately captures scope, files, requirements, acceptance criteria, and validation strategy before execution.

Risk: User-facing progress is intentionally reported in Portuguese (pt-BR).

Mitigation: Use the skill in contexts where Portuguese progress reports are acceptable, or adjust the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/execute-specs)
- [Publisher metadata repository](https://github.com/afonsoft/skills)
- [Good and Bad Tests](references/tests.md)
- [When to Mock](references/mocking.md)
- [Refactor Candidates](references/refactoring.md)
- [Deep Modules](references/deep-modules.md)
- [Interface Design for Testability](references/interface-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code and shell commands, plus code and test changes in the workspace when execution proceeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing progress and explanations are in Portuguese (pt-BR); internal reasoning and commands remain in English.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
