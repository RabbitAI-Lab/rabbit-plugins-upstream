## Description:

Enforces fresh verification evidence before claiming work is complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to check scope, run claim-matched verification, and report supported outcomes before handing off work or declaring it done.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification may take additional time and resources.

Mitigation: Use when stronger completion evidence is warranted and run checks relevant to the claim.

Risk: Destructive test or migration commands could alter persistent data.

Mitigation: Confirm their effective targets are disposable test environments before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Verification strategies by change type](references/change-strategies.md)
- [Claims and failures](references/claims-and-failures.md)
- [Isolated verification](references/isolated-verification.md)
- [Proof integrity](references/proof-integrity.md)
- [Scope and sweeps](references/scope-and-sweeps.md)
- [System-wide test check](references/system-wide-test-check.md)
- [Verification oracles](references/verification-oracles.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with verification outcomes and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports failed or skipped checks and material remaining risks.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
