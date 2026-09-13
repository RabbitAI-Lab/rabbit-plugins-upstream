## Description:

Postgres AIops helps agents operate and troubleshoot PostgreSQL clusters as a DBA, including health checks, query and index diagnostics, lock analysis, replication checks, and governed maintenance writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and database administrators use this skill to inspect PostgreSQL cluster health, diagnose slow queries, bloat, locks, and replication issues, and plan or execute guarded maintenance operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live PostgreSQL changes, including terminating sessions, dropping indexes, and changing server settings.

Mitigation: Start with a dedicated read-only PostgreSQL role and enable write-capable credentials only for planned maintenance where those actions are acceptable.

Risk: Credential and local state exposure could affect database access because the skill stores configuration and encrypted secrets locally.

Mitigation: Protect POSTGRES_AIOPS_HOME and POSTGRES_AIOPS_MASTER_PASSWORD, keep the local state directory access-restricted, and migrate away from legacy plaintext password environment variables.

Risk: A reproducible pinned install is not enforced by the skill evidence.

Mitigation: Verify the postgres-aiops package source and version before installation, and pin the package version where the runtime supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/postgres-aiops)
- [Project homepage](https://github.com/AIops-tools/Postgres-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like tool result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run SQL previews, RCA findings, audit and undo guidance, and PostgreSQL configuration steps.]

## Skill Version(s):

0.10.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
