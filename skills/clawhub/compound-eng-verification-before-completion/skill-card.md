## Description:

Enforces fresh verification evidence before an agent claims tests pass, a bug is fixed, work is done, a release is ready, or similar completion states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to choose and run claim-matched verification before completing code, release, handoff, or review work. It is especially useful when task scope is ambiguous, a dirty worktree could contaminate evidence, or a success claim depends on tests, builds, linting, security checks, diff review, or live exercise of an entry point.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add clarification and verification steps to routine coding workflows.

Mitigation: Use it when completion, handoff, release, or review claims require fresh evidence, and scope checks to the project-declared gates that apply to the specific action.

Risk: An agent could still under-verify if it chooses a command that does not exercise the claimed behavior.

Mitigation: Require claim-matched proof through the intended entry point, read the full output and exit status, and report skipped or narrower checks explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion)
- [Specification](SPEC.md)
- [Change Strategies](references/change-strategies.md)
- [Claims and Failures](references/claims-and-failures.md)
- [Isolated Verification](references/isolated-verification.md)
- [Proof Integrity](references/proof-integrity.md)
- [Scope and Sweeps](references/scope-and-sweeps.md)
- [System-Wide Test Check](references/system-wide-test-check.md)
- [Verification Oracles](references/verification-oracles.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to report verification commands, outcomes, skipped checks, and material residual risks.]

## Skill Version(s):

4.5.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
