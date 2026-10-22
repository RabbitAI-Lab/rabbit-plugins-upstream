## Description:

Audits whether tests detect regressions in the behavior they claim to protect, including weak assertions, mocked-away subjects, and gaps in test gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and test reviewers use this workflow to assess whether existing tests catch credible behavioral regressions and to identify ineffective, partially effective, or unenforced tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit probes or mutations may change a repository or affect external services.

Mitigation: Default to read-only review; run instrumentation and mutations only in isolated scratch copies, and use paid APIs, network services, or shared databases only with explicit authorization and isolation.

Risk: Heuristic detector results or a surviving mutation may overstate a test-quality gap.

Mitigation: Review the claimed behavior and neighboring tests, confirm findings against a concrete counterexample, and disclose limits of the audit scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-test-audit)
- [Behavioral review](references/behavioral-review.md)
- [Detector diagnostics and blind spots](references/detectors.md)
- [Mutation probes and repairs](references/mutation-and-repair.md)
- [Per-stack commands](references/stacks.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown audit findings with test locations, evidence status, and suggested repairs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes confirmed findings from unresolved candidates and reports scope and commands run.]

## Skill Version(s):

5.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
