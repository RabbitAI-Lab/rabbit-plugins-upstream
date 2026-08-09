## Description:

Chinese-language Java unit test guidance skill that helps developers design, review, and implement focused unit tests using equivalence classes, boundary values, decision tables, state-transition analysis, JUnit, Mockito, and related Java testing conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baixuanzhu](https://clawhub.ai/user/baixuanzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, or completing Java unit tests for application code. It helps choose test cases, decide how many tests are enough, map designs into JUnit or Mockito code, and avoid common unit-test design mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test code or review guidance can be incorrect or incomplete for the target project.

Mitigation: Review proposed tests against the method contract, run the project's test suite, and confirm the positive, negative, boundary, and exception cases are genuinely representative.

Risk: The skill may suggest adding or using testing dependencies such as AssertJ, JaCoCo, Mockito, or ArchUnit.

Mitigation: Check dependency changes against the project's existing stack and approval process before applying them.

Risk: The skill is scoped to unit-test guidance and can be misapplied to integration, E2E, performance, or frontend testing work.

Mitigation: Use a dedicated testing approach for those out-of-scope scenarios and keep this skill focused on Java unit tests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baixuanzhu/skills/java-unit-test)
- [Test Design Foundations](references/01-test-design-foundations.md)
- [Equivalence and Boundary Analysis](references/02-equivalence-and-boundary.md)
- [Decision Table Testing](references/03-decision-table.md)
- [State Transition Testing](references/04-state-transition.md)
- [Coverage and Test Quantity](references/05-coverage-and-quantity.md)
- [Java Unit Test Tooling](references/06-tools-lean.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Java code snippets, tables, dependency snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language guidance scoped to Java unit tests; excludes integration, E2E, performance, and frontend testing.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
