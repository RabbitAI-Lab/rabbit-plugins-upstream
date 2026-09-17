## Description:

Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to plan, execute, prove, and roll back major migrations or upgrades for stateful OpenClaw agents while preserving state, credentials, automations, plugins, and local embeddings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact operational migration steps can affect production state, service availability, and rollback integrity.

Mitigation: Use the skill only for real OpenClaw stateful migrations or upgrades, and follow its backup, rehearsal, proof, and rollback gates before changing production state.

Risk: Proposed mutations such as service fencing, restarts, repairs, and rollback actions may be unsafe if applied without operator review.

Mitigation: Review each mutation before running it on production state and preserve redacted evidence for acceptance or rollback decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/posthuman/skills/stateful-agent-migration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, checklists, and status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes redacted evidence, verified backups, rehearsal, live proof, and explicit rollback readiness.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
