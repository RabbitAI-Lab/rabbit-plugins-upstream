## Description:

Enforces fresh verification evidence before any completion claim. Use when about to claim "tests pass", "bug fixed", "done", "ready to merge", handing off work, or before editing when a request has ambiguous scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before reporting work complete or handing it off. It guides them to choose fresh checks that match the claim, preserve authorized scope, and report what the evidence establishes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tests or migrations may affect a development or shared service if their targets are not disposable.

Mitigation: Confirm database and service targets are disposable before running suites or migrations; use a dedicated test database, container, or throwaway schema.

Risk: A completion claim may overstate what an earlier or incomplete check proves.

Mitigation: Run fresh checks matched to the claim, then inspect complete output, exit status, and relevant failure paths before reporting results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Proof integrity](artifact/references/proof-integrity.md)
- [Verification oracles](artifact/references/verification-oracles.md)
- [Claims and failures](artifact/references/claims-and-failures.md)
- [Change strategies](artifact/references/change-strategies.md)
- [Scope and sweeps](artifact/references/scope-and-sweeps.md)
- [System-wide test checks](artifact/references/system-wide-test-check.md)
- [Performance measurement](artifact/references/performance-measurement.md)
- [Isolated verification](artifact/references/isolated-verification.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with inline shell commands and verification checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

5.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
