## Description:

Audits whether tests detect regressions in their claimed behavior, identifying false confidence from mocks, weak assertions, undiscriminating fixtures, swallowed failures, and gaps in test gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit test suites for false confidence, identify tests that would survive meaningful regressions, and report actionable findings with their evidence and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutation and reach probes can execute tests with external side effects or modify source files.

Mitigation: Run probes in an isolated scratch copy, and exclude paid APIs and shared databases unless separately authorized and isolated.

Risk: Heuristic detector matches may overstate test weaknesses or miss them.

Mitigation: Treat detector output as leads; confirm findings against the test and production source, and document unresolved limitations.

## Reference(s):

- [Behavioral review](references/behavioral-review.md)
- [Detector diagnostics and blind spots](references/detectors.md)
- [Mutation probes and repairs](references/mutation-and-repair.md)
- [Per-stack commands](references/stacks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown audit report with evidence, counterexamples, limitations, and repair directions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates confirmed findings from unresolved candidates and records commands not run.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
