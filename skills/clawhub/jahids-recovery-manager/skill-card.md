## Description:

Plan safe recovery from failed or partial agent tasks using checkpoints, idempotency, rollback, and evidence preservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdjahid11978-design](https://clawhub.ai/user/mdjahid11978-design)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to plan recovery after a task fails, times out, partially completes, or leaves external state uncertain. It guides checkpoint identification, state reconciliation, rollback or compensation, and verification within the original authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrying an operation before confirming whether it already succeeded can create duplicate or inconsistent external changes.

Mitigation: Reconcile external state and check idempotency before retrying.

Risk: Recovery actions could exceed the original task's authorization or rely on expired approval.

Mitigation: Keep recovery within the original authorization and remaining budget; do not reuse expired approval.

## Reference(s):

- [Server-resolved source repository](https://github.com/mdjahid11978-design/Jahids-skills/tree/main/skills/jahids-recovery-manager)
- [ClawHub skill release](https://clawhub.ai/mdjahid11978-design/skills/jahids-recovery-manager)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown recovery plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checkpoint, state reconciliation, rollback or compensation, and verification steps.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
