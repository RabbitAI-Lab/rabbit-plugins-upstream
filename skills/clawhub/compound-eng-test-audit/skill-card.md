## Description:

Audits whether tests detect regressions in the behaviors they claim to protect, including weak assertions, mocked-away subjects, and tests missing from enforcement gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review test suites for false confidence, establish whether claimed behaviors are exercised and asserted, and report actionable regression-sensitivity findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit commands may read repository source and tests or execute local test code.

Mitigation: Limit repository access to the approved scope and review commands before running them.

Risk: Mutation and reach probes can change files or trigger external services during test execution.

Mitigation: Run probes in an isolated scratch copy; avoid live services, paid APIs, and shared databases without separate authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-test-audit)
- [Behavioral review](references/behavioral-review.md)
- [Detector diagnostics and blind spots](references/detectors.md)
- [Mutation probes and repairs](references/mutation-and-repair.md)
- [Per-stack commands](references/stacks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit findings with test locations, surviving regressions, evidence status, and commands where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; distinguishes confirmed findings from unresolved candidates.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
