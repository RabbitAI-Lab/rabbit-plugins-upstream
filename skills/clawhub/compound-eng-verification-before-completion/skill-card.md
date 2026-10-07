## Description:

Enforces fresh, claim-matched verification before an agent reports engineering work complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to choose relevant checks, inspect fresh results, and make completion or handoff claims no broader than the evidence supports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification commands or migrations can change persistent project data.

Mitigation: Confirm tests, migrations, and service checks target disposable databases, containers, or schemas before running them.

Risk: A green but empty or partial test run can produce an unsupported completion claim.

Mitigation: Inspect exit status, executed counts, command identity, and requirement coverage; disclose checks that did not run.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Proof integrity](artifact/references/proof-integrity.md)
- [Verification oracles](artifact/references/verification-oracles.md)
- [Isolated verification](artifact/references/isolated-verification.md)
- [Change strategies](artifact/references/change-strategies.md)
- [Scope and sweeps](artifact/references/scope-and-sweeps.md)
- [System-wide test check](artifact/references/system-wide-test-check.md)
- [Claims and failures](artifact/references/claims-and-failures.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown prose with verification commands and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks run, failures or skipped checks, proof scope, and residual risks.]

## Skill Version(s):

5.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
