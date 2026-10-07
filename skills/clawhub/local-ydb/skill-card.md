## Description:

Helps developers operate, troubleshoot, and harden Local YDB deployments, including Docker setups, schemas, monitoring, authentication, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[astandrik](https://clawhub.ai/user/astandrik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to plan, inspect, and maintain Local YDB environments, including schema changes, tenant health, authentication, and storage migration. Live operations require access to the target environment and confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Docker removal, storage cleanup, and schema application can disrupt or delete data.

Mitigation: Review the plan, backups, rollback, and verification before approving destructive actions.

Risk: Authentication changes and password rotation can lock out clients or expose credentials.

Mitigation: Review credential handling and access checks before approving changes; keep secrets out of shared output.

Risk: Public monitoring exposure can reveal operational data.

Mitigation: Review access controls and endpoint exposure before publishing monitoring routes.

## Reference(s):

- [Local YDB Toolkit release](https://clawhub.ai/astandrik/skills/local-ydb)
- [Topology reference](artifact/references/topology.md)
- [Auth hardening reference](artifact/references/auth-hardening.md)
- [Storage migration reference](artifact/references/storage-migration.md)
- [Verification reference](artifact/references/verification.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans include impact, verification, and rollback steps for live changes.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
