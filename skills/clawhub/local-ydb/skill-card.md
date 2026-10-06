## Description:

Helps developers operate, troubleshoot, and harden local YDB deployments, including Docker topology, SQL, schemas, authentication, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[astandrik](https://clawhub.ai/user/astandrik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage local YDB deployments, generate and review table schemas, and plan verified changes to authentication, storage, and monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destroy, cleanup, or storage migration could cause data loss or disrupt a local YDB deployment.

Mitigation: Review the plan before confirmation; retain dumps and rollback steps, then verify restored data and storage placement before deleting old resources.

Risk: Authentication or public monitoring changes could expose credentials or services.

Mitigation: Keep password files and dumps out of shared repositories, use protected monitoring access, and verify authentication after changes.

Risk: Tests or generated commands could alter an unintended deployment.

Mitigation: Use disposable profiles for tests and confirm the selected target and impact before applying changes.

## Reference(s):

- [Local YDB Toolkit release](https://clawhub.ai/astandrik/skills/local-ydb)
- [Topology and deployment guidance](references/topology.md)
- [Authentication hardening](references/auth-hardening.md)
- [Storage migration](references/storage-migration.md)
- [Verification procedures](references/verification.md)
- [SQL and schema tool scenarios](references/mcp-tool-scenarios.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command, configuration, and SQL snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live changes require a reviewed plan, confirmation, rollback, and verification.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
