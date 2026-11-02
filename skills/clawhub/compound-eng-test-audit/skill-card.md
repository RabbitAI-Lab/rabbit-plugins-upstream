## Description:

Audit whether tests detect regressions in the behavior they claim to protect. Find mocked-away subjects, weak or circular assertions, undiscriminating fixtures, swallowed failures, and tests missing from gates. Use for test-quality audits, suspected false confidence in generated tests, and reviewing new tests. Use ia-writing-tests for writing tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and test owners use this workflow to audit whether a test suite detects regressions in the behaviors its tests claim to protect, and to produce actionable findings with evidence and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional recording probe can disrupt tests if logging fails, and its local reports may include snippets of test error output.

Mitigation: Run the probe in an isolated scratch copy with a fresh, writable temporary report directory; handle generated reports as potentially containing test error details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-test-audit)
- [Behavioral review guide](artifact/references/behavioral-review.md)
- [Detector diagnostics and blind spots](artifact/references/detectors.md)
- [Mutation probes and repairs](artifact/references/mutation-and-repair.md)
- [Per-stack commands](artifact/references/stacks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown audit report with findings, evidence, scope, and limitations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include unresolved candidates, retained counterexamples, and commands or results when available.]

## Skill Version(s):

5.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
