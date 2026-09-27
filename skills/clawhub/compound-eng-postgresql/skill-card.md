## Description:

Provides PostgreSQL guidance for schema design, query optimization, indexing, migrations, security, and operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to design PostgreSQL schemas, review queries and indexes, plan safe migrations, and address concurrency, security, and operational concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SQL, migrations, or operational commands could disrupt data or availability if applied without review.

Mitigation: Review changes, test on staging with representative data, maintain backups, and follow production change controls before execution.

## Reference(s):

- [Schema and migration safety](artifact/references/schema-and-migrations.md)
- [Query and index patterns](artifact/references/query-and-index-patterns.md)
- [Security and operations](artifact/references/security-and-operations.md)
- [PostgreSQL operations](artifact/references/operations.md)
- [Concurrency patterns](artifact/references/concurrency-patterns.md)
- [PostgreSQL full-text search](artifact/references/full-text-search.md)
- [Performance patterns](artifact/references/performance-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with SQL and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations require review against the target database and workload.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
