## Description:

Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to rehearse, perform, and verify stateful OpenClaw agent upgrades while protecting live state and preserving a rollback path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stopping services or changing plugin and service records can interrupt a live agent.

Mitigation: Rehearse the cutover and rollback, verify a recovery point, and prove live health before resuming writers.

Risk: Backups, credential checks, and migration artifacts may expose secrets or user content.

Mitigation: Keep backups private and record only redacted categories, counts, and hashes.

## Reference(s):

- [Stateful Agent Migration on ClawHub](https://clawhub.ai/posthuman/skills/stateful-agent-migration)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacted migration checks, acceptance results, and rollback status.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
