## Description:

Requires fresh, claim-matched verification evidence before an agent reports engineering work complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to verify changes with fresh, relevant checks before claiming tests pass, a bug is fixed, or work is ready to hand off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tests or migrations may change data when run against a non-disposable database or service.

Mitigation: Confirm verification targets are disposable before running checks; stop and request a safe environment otherwise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Proof integrity](artifact/references/proof-integrity.md)
- [Verification strategies by change type](artifact/references/change-strategies.md)
- [Claims and failures](artifact/references/claims-and-failures.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Verification guidance]

**Output Format:** [Markdown with verification commands, outcomes, and remaining risks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims are limited to fresh checks actually run; failed or skipped checks are disclosed.]

## Skill Version(s):

5.1.2 (source: ClawHub release record)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
