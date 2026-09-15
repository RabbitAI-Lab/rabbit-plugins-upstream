## Description:

Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, rehearse, execute, prove, and roll back major migrations of stateful OpenClaw agents while preserving service ownership, credentials, backups, plugins, and local memory identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration guidance can affect live state, backups, service restarts, and rollback paths if executed without supervision.

Mitigation: Use only for planned OpenClaw migrations with operator review of each live mutation; keep backups private and verify restore and rollback readiness before cutover.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces redacted migration checklists, command sequences, acceptance gates, rollback criteria, and final PASS/BLOCKED/ROLLED BACK status guidance.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
