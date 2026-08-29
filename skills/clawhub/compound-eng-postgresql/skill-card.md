## Description:

PostgreSQL schema design, query optimization, indexing, and administration for work involving PostgreSQL, JSONB, partitioning, RLS, CTEs, window functions, or EXPLAIN ANALYZE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill for PostgreSQL schema design, migrations, indexing, query optimization, row-level security, full-text search, connection pooling, operations, and recovery planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SQL examples, migration patterns, RLS policies, failover steps, backup procedures, and full-text-search language settings may be unsafe if copied directly into a production database without adaptation.

Mitigation: Review and test examples against the target schema and workload before applying them, especially for migrations, production operations, and security policies.

Risk: Schema changes, backfills, index creation, and read-modify-write loops can lock tables, rewrite data, or drop concurrent writes if applied without the documented safeguards.

Mitigation: Use the skill's migration safety guidance, including concurrent index creation, batched backfills, atomic updates, row-level locks, or compare-and-swap retries where appropriate.

Risk: Operational settings for replication, WAL, autovacuum, timeouts, and connection pools can affect availability or recovery objectives.

Mitigation: Validate operational recommendations in staging, monitor PostgreSQL metrics, and align backup, replication, and pool sizing decisions with production service requirements.

## Reference(s):

- [PostgreSQL Skill Definition](SKILL.md)
- [ia-postgresql Specification](SPEC.md)
- [Concurrency Patterns](references/concurrency-patterns.md)
- [PostgreSQL Full-Text Search](references/full-text-search.md)
- [PostgreSQL Operations](references/operations.md)
- [Performance Patterns](references/performance-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline SQL and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory PostgreSQL guidance and examples; it does not execute commands or modify databases on its own.]

## Skill Version(s):

4.4.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
