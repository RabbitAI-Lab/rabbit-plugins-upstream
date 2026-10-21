## Description:

Guides agents in writing and reviewing behavioral tests with meaningful assertions, sound fixtures, and reliable regression checks across languages and frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write, improve, and review tests that verify observable behavior, catch regressions, and report actual test outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running project tests or state-resetting fixtures may alter local test data.

Mitigation: Inspect test configuration and isolate stateful test resources before executing project commands.

Risk: Mock-heavy or skipped tests can create misleading confidence in coverage.

Mitigation: Check observable assertions and executed-test counts, and report any omissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Test design](artifact/references/test-design.md)
- [Regression proof](artifact/references/regression-proof.md)
- [Test completion](artifact/references/test-completion.md)
- [Test smells](artifact/references/test-smells.md)

## Skill Output:

**Output Type(s):** [Code, Guidance, Shell commands]

**Output Format:** [Test code and Markdown guidance with project-specific commands and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the repository's test runner and existing contracts; distinguishes executed tests from skipped or unrun tests.]

## Skill Version(s):

5.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
