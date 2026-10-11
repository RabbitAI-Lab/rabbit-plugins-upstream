## Description:

Guides developers in writing behavioral tests with meaningful assertions, regression checks, and resistance to common test-quality pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when writing or improving tests, adding coverage, or reproducing bugs across languages and frameworks. It helps them select discriminating cases, check observable outcomes, and report what was actually verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running real test commands or controlled red/green checks may modify shared test state.

Mitigation: Review commands before running them, use isolated fixtures or disposable test data, and restore temporary control changes.

Risk: Weak assertions or unreviewed expected-output changes can make a broken behavior appear correct.

Mitigation: Check tests against observable behavior and the intended failure; review any specification or golden-output change separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Test design](references/test-design.md)
- [Regression proof](references/regression-proof.md)
- [Test smells](references/test-smells.md)
- [Oracle smells](references/oracle-smells.md)
- [Isolation and sandbox traps](references/isolation-and-sandbox-traps.md)
- [False-pass oracle traps](references/false-pass-oracle-traps.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test results, failures, and untested cases.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
