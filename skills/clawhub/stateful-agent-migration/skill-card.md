## Description:

Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to plan and execute major OpenClaw stateful agent migrations or upgrades while preserving state, credentials, embeddings, service ownership, and rollback readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact live migration guidance could affect production state or service availability if applied without review.

Mitigation: Review the migration plan before live cutover and require human approval before repairs or service changes in production.

Risk: Backups and migration artifacts may contain sensitive state, credentials, or user content.

Mitigation: Keep backups private, use redacted category/count/hash evidence in reports, and avoid recording credentials, raw config, transcripts, messages, or SQLite rows.

Risk: Unpaused writers or supervisors can mutate state during migration and undermine rollback or proof gates.

Mitigation: Inventory, pause, and resume writers explicitly, require a quiet window before cutover, and keep rollback readiness until live proof passes.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
