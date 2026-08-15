## Description:

Generates pytest tests that follow a Python project's conventions, including fixtures, mocks, parametrization, edge cases, and coverage-gap notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft pytest test suites for Python code that match existing project conventions, cover common edge cases, and identify remaining coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated tests may encode an incorrect assumption about intended behavior.

Mitigation: Review generated tests before applying them and run them in the project test environment before relying on coverage results.

Risk: Generated fixtures or mocks for databases, authentication helpers, or external services may need project-specific safety boundaries.

Mitigation: Inspect fixture and mock code before use, prefer isolated test resources, and avoid connecting generated tests to production services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/pytest-generator-pro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with Python code blocks and coverage tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated tests are draft pytest code and conftest additions; the skill does not run tests.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
