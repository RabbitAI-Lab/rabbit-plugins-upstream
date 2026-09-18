## Description:

Postgres AIops helps agents operate and troubleshoot PostgreSQL clusters with health checks, catalog and pg_stat reads, RCA analyses for slow queries, bloat/vacuum and blocking locks, and governed DBA write commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and operations engineers use this skill to inspect PostgreSQL health, diagnose slow queries, bloat, autovacuum, replication, and blocking locks, and prepare or run governed maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke powerful PostgreSQL state-changing operations without an enforced approval gate.

Mitigation: Connect with a read-only pg_monitor-style role by default, require a separate human approval process for destructive operations, and reserve elevated privileges for approved maintenance windows.

Risk: The release evidence flags installation of an unpinned external implementation.

Mitigation: Use a pinned, reviewed postgres-aiops package version and run the skill from an isolated account or container.

Risk: Database credentials and audit state are local operational assets that can expose or affect production systems if mishandled.

Mitigation: Set POSTGRES_AIOPS_HOME to a protected location, protect the master password, and verify filesystem permissions before connecting to sensitive databases.

## Reference(s):

- [postgres-aiops capabilities](references/capabilities.md)
- [postgres-aiops CLI reference](references/cli-reference.md)
- [postgres-aiops setup & security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Postgres AIops GitHub repository](https://github.com/AIops-tools/Postgres-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/postgres-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured database findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk-tiered recommendations, dry-run commands, and notes when source database reads are truncated.]

## Skill Version(s):

0.10.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
