## Description:

Requires fresh, claim-matched verification before an agent reports engineering work as complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to check the relevant requirements, tests, and other project gates before claiming a change is finished or ready to hand off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification suites or migrations could affect non-disposable databases or external services.

Mitigation: Confirm targets are disposable before running checks; request a safe environment when they are not.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Change strategies](references/change-strategies.md)
- [Claims and failures](references/claims-and-failures.md)
- [Isolated verification](references/isolated-verification.md)
- [Proof integrity](references/proof-integrity.md)
- [Scope and sweeps](references/scope-and-sweeps.md)
- [System-wide test check](references/system-wide-test-check.md)
- [Verification oracles](references/verification-oracles.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown text with verification results and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the evidence supporting each completion claim, skipped checks, and remaining risks.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
