## Description:

Enforces fresh verification evidence before any completion claim, including tests, bug fixes, release readiness, handoffs, and ambiguous-scope work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to require fresh, claim-matched verification before reporting work as complete. It is most useful for test, build, bug-fix, release-readiness, handoff, and broad-scope engineering claims where stale or partial evidence would be misleading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could claim completion from stale, partial, or unrelated evidence.

Mitigation: Run fresh, claim-matched verification immediately before the claim and report the exact command, URL, or interaction path that supports it.

Risk: Ambiguous task scope could lead to editing or verifying the wrong part of a repository.

Mitigation: Inspect the repository first, state a safe assumption when one interpretation is clear, and ask for clarification when materially different scopes remain.

Risk: A dirty worktree or weak oracle could mask regressions or produce misleading green results.

Mitigation: Check working tree state, preserve unrelated changes, use isolated verification for shared-module changes, and require positive controls for empty or absence-based results.

## Reference(s):

- [Skill source](SKILL.md)
- [Specification](SPEC.md)
- [Change Strategies](references/change-strategies.md)
- [Claims and Failures](references/claims-and-failures.md)
- [Isolated Verification](references/isolated-verification.md)
- [Proof Integrity](references/proof-integrity.md)
- [Scope and Sweeps](references/scope-and-sweeps.md)
- [System-Wide Test Check](references/system-wide-test-check.md)
- [Verification Oracles](references/verification-oracles.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples and concise completion reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verification scope, exercised command or path, failed or skipped checks, and material residual risks when relevant.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
