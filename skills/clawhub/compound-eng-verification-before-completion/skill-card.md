## Description:

Enforces fresh verification evidence before any completion claim, including test, fix, and handoff claims, and prompts scope clarification before ambiguous edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to choose and run claim-matched checks before reporting work complete, while preserving unrelated changes and disclosing verification gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification checks or migrations may affect a non-disposable database, service, or unrelated local changes.

Mitigation: Confirm targets are disposable and the requested scope is authorized before running checks; stop and clarify when they are not.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Proof integrity](artifact/references/proof-integrity.md)
- [Change verification strategies](artifact/references/change-strategies.md)
- [Verification oracles](artifact/references/verification-oracles.md)
- [Claims and failures](artifact/references/claims-and-failures.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with commands and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks performed, skipped checks, and residual risks.]

## Skill Version(s):

5.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
