## Description:

PostgreSQL schema design, query optimization, indexing, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to design and review PostgreSQL schemas, queries, indexes, migrations, and operational practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Failover guidance, especially pg_rewind, could lead to PostgreSQL data loss if the wrong cluster is treated as authoritative.

Mitigation: Before pg_rewind, confirm which cluster is authoritative and preserve and reconcile any data that could be lost.

Risk: The scanner reported a possible mismatch between the skill's stated purpose and evaluation commands, with partial coverage because one local reference could not be resolved.

Mitigation: Review the unresolved reference and check evaluation commands against the intended PostgreSQL task before running them.

## Reference(s):

- [ia-postgresql on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)
- [Schema and migrations](artifact/references/schema-and-migrations.md)
- [Query and index patterns](artifact/references/query-and-index-patterns.md)
- [Security and operations](artifact/references/security-and-operations.md)
- [Operations](artifact/references/operations.md)
- [Concurrency patterns](artifact/references/concurrency-patterns.md)
- [PostgreSQL serialization failure handling](https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html)
- [PostgreSQL multicolumn indexes](https://www.postgresql.org/docs/18/indexes-multicolumn.html)
- [PostgreSQL client runtime configuration](https://www.postgresql.org/docs/18/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT)
- [PostgreSQL ALTER TABLE reference](https://www.postgresql.org/docs/18/sql-altertable.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with SQL code blocks, tables, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context-dependent examples; no fixed response schema.]

## Skill Version(s):

5.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
