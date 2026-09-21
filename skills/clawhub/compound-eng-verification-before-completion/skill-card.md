## Description:

Enforces fresh verification evidence before any completion claim, including claims that tests pass, bugs are fixed, work is done, a release is ready, or ambiguous scope has been resolved before editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill before reporting completion, committing, pushing, opening a PR, or handing off work. It helps match verification commands to the actual claim, preserve unrelated work, avoid weakened proof, and report only what current evidence supports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make an agent more cautious about broad scope, dirty worktrees, and failed checks, which may slow completion when verification evidence is incomplete.

Mitigation: Apply the skill when completion claims or handoffs need proof, and keep reports concise by naming only the command or path exercised, observed result, skipped or failed checks, and material residual risk.

Risk: A green local run can be misleading when unrelated work, stale binaries, empty test runs, or weakened assertions make the verification easier to satisfy.

Mitigation: Use the artifact's guidance to inspect the worktree, preserve unrelated changes, confirm the invoked binary or entry point, require positive executed counts, and avoid changing the oracle solely to obtain a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Specification](artifact/SPEC.md)
- [Proof integrity](artifact/references/proof-integrity.md)
- [Verification oracles](artifact/references/verification-oracles.md)
- [Change strategies](artifact/references/change-strategies.md)
- [Claims and failures](artifact/references/claims-and-failures.md)
- [Scope and sweeps](artifact/references/scope-and-sweeps.md)
- [Isolated verification](artifact/references/isolated-verification.md)
- [System-wide test check](artifact/references/system-wide-test-check.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Analysis]

**Output Format:** [Markdown guidance with inline shell commands and concise completion reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should name the verification command or path exercised, observed result, skipped or failed checks, and material residual risk.]

## Skill Version(s):

4.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
