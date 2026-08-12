## Description:

Postgres AIops helps agents inspect and operate PostgreSQL clusters with governed DBA workflows for health checks, slow-query root-cause analysis, bloat and vacuum analysis, blocking locks, replication, and audited maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Database administrators, SREs, and agent developers use this skill to triage PostgreSQL health, analyze slow queries, table bloat, autovacuum lag, locks, and replication status, and run audited maintenance commands when an appropriate database role permits them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real PostgreSQL changes when connected with a privileged database role.

Mitigation: Start with a read-only or pg_monitor-style role and grant write or DDL privileges only for targets where agent-driven maintenance is acceptable.

Risk: Database credentials and POSTGRES_AIOPS_MASTER_PASSWORD are sensitive secrets.

Mitigation: Protect the master password like any other secret and use the encrypted postgres-aiops secret store rather than plaintext credentials.

Risk: Some operations, including cancel, terminate, vacuum, reindex, and query-stat resets, cannot restore the prior database state.

Mitigation: Use dry-run previews, confirm the target object or backend pid, and prefer reversible operations or recorded undo flows where the tool supports them.

Risk: The tool records and previews operations but does not decide whether a write is authorized.

Mitigation: Rely on database role permissions, deployment policy, and agent approval rules to control which operations may run.

## Reference(s):

- [Capabilities Reference](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup and Security Guide](artifact/references/setup-guide.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Project Homepage](https://github.com/AIops-tools/Postgres-AIops)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/postgres-aiops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP and CLI workflows may return result envelopes with limits and truncation flags; maintenance actions can include dry-run previews, audit records, and undo metadata where supported.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
