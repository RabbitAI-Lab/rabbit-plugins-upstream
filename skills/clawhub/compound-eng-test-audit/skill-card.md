## Description:

Audits whether tests detect regressions in the behavior they claim to protect, including weak assertions, mocked-away subjects, and tests missing from gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and test reviewers use this skill to identify tests that can pass despite regressions, distinguish confirmed weaknesses from leads, and recommend targeted repairs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Static detector leads may be mistaken for confirmed test weaknesses.

Mitigation: Trace the real behavior and assertions, check detector completeness, and label findings by evidence status.

Risk: Reach or mutation probes may execute repository tests that access credentials, networks, paid APIs, databases, or local services.

Mitigation: Run probes only in an isolated scratch copy or disposable environment and keep external services out unless separately authorized and isolated.

## Reference(s):

- [Behavioral review](artifact/references/behavioral-review.md)
- [Detector diagnostics and blind spots](artifact/references/detectors.md)
- [Mutation probes and repairs](artifact/references/mutation-and-repair.md)
- [Per-stack commands](artifact/references/stacks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown audit report with findings, evidence status, and repair directions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes reviewed scope, concrete surviving regressions, retained protections, and unrun checks.]

## Skill Version(s):

5.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
