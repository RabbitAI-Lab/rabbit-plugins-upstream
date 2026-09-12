## Description:

Guides developers through SPEC-approved test-driven development by turning requirements and acceptance criteria into mapped red-green-refactor vertical slices with Portuguese user-facing communication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to implement approved feature or bugfix SPECs through a disciplined red-green-refactor workflow. It maps each test to numbered requirements or acceptance criteria, validates each vertical slice, and keeps user-facing communication in Portuguese (pt-BR).

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referenced slash-command dependencies may not exist in every target environment.

Mitigation: Review availability of `/grill-me-with-spec` and `/qa-analyst` before relying on those handoffs.

Risk: Using the workflow with a missing, draft, or incomplete SPEC could lead to tests or implementation that do not match the intended requirement.

Mitigation: Require an approved SPEC, map each test to an RF or AC identifier, and run the full affected test, lint, and type-check suite after each slice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/tdd-spec)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Project metadata URL](https://github.com/afonsoft/skills)
- [Good and Bad Tests](tests.md)
- [When to Mock](mocking.md)
- [Refactor Candidates](refactoring.md)
- [Deep Modules](deep-modules.md)
- [Interface Design for Testability](interface-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown with code snippets, test guidance, status reports, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing questions, recommendations, and progress reports are in Portuguese (pt-BR).]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
