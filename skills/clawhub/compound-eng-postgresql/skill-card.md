## Description:

Provides PostgreSQL guidance for schema design, queries, indexing, migrations, security, and operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to plan and review PostgreSQL schemas, migrations, queries, indexes, access controls, and operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SQL may alter or delete production data or cause long-running locks.

Mitigation: Review against the PostgreSQL version, data size, lock budget, and migration policy; run destructive or write-heavy examples only with explicit authorization and rollback planning.

Risk: Search behavior may differ across languages and locales.

Mitigation: Validate search configuration and examples against the application's language and locale requirements before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)
- [Schema and migration safety](artifact/references/schema-and-migrations.md)
- [Query and index patterns](artifact/references/query-and-index-patterns.md)
- [Security and operations](artifact/references/security-and-operations.md)
- [Concurrency patterns](artifact/references/concurrency-patterns.md)
- [PostgreSQL operations](artifact/references/operations.md)
- [Performance patterns](artifact/references/performance-patterns.md)
- [PostgreSQL full-text search](artifact/references/full-text-search.md)
- [PostgreSQL statement timeout documentation](https://www.postgresql.org/docs/18/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT)
- [PostgreSQL ALTER TABLE documentation](https://www.postgresql.org/docs/18/sql-altertable.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with SQL and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output; review before applying database changes.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
