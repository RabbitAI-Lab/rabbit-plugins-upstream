## Description:

Guides an agent through an approved SPEC using test-driven development, converting requirements and acceptance criteria into red-green-refactor implementation slices while reporting to the user in Portuguese.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to implement an approved SPEC through small TDD slices, mapping each test to a requirement or acceptance criterion and validating after each change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit code and tests from an approved SPEC without asking for approval between each TDD slice.

Mitigation: Review the SPEC before starting, run the work on a branch or disposable worktree, and inspect the final diff before merging.

Risk: The skill runs project validation commands such as tests, lint, type checks, and relevant end-to-end checks.

Mitigation: Use it in a development environment appropriate for running repository commands, with normal secrets and network controls in place.

Risk: User-facing progress, questions, and recommendations are expected to be in Portuguese.

Mitigation: Install it only where Portuguese user-facing communication matches the team or user workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/execute-tdd-spec)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Metadata URL](https://github.com/afonsoft/skills)
- [tests.md](tests.md)
- [mocking.md](mocking.md)
- [refactoring.md](refactoring.md)
- [deep-modules.md](deep-modules.md)
- [interface-design.md](interface-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown progress reports with code, test, and validation changes produced in the workspace]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing questions and recommendations are in Portuguese (pt-BR).]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
