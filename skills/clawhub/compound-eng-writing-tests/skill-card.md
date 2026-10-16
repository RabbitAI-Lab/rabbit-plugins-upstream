## Description:

Guides agents to write discriminating behavioral tests, use meaningful assertions, avoid common testing anti-patterns, and verify that test suites actually exercise the intended behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to add or improve test coverage, reproduce bugs, and verify that tests detect meaningful regressions across languages and frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weak assertions or skipped tests can create false confidence.

Mitigation: Use discriminating assertions and inspect executed and passed test counts.

Risk: Running project tests may change shared test state or fixtures.

Mitigation: Inspect project test commands and use isolated temporary files and test databases where appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Test design](references/test-design.md)
- [Regression proof](references/regression-proof.md)
- [Test smells](references/test-smells.md)
- [Test completion](references/test-completion.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Project-specific test code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports tests exercised, actual results, failures, and omissions.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
