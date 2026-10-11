## Description:

Provides PostgreSQL guidance for schema design, migrations, query optimization, indexing, security, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to design and review PostgreSQL schemas, migrations, queries, indexes, access controls, and operational procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SQL could change or damage production data if run without review.

Mitigation: Review SQL and run write queries only when authorized and safe; use disposable data for testing where possible.

Risk: EXPLAIN ANALYZE executes the underlying query and may cause side effects.

Mitigation: Start with EXPLAIN; run EXPLAIN ANALYZE only when execution and its effects are authorized and safe.

Risk: A mismatched full-text configuration can produce incorrect search results for a locale.

Mitigation: Choose and test the appropriate locale-specific full-text configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)
- [Schema and migration safety](artifact/references/schema-and-migrations.md)
- [Query and index patterns](artifact/references/query-and-index-patterns.md)
- [Security and operations](artifact/references/security-and-operations.md)
- [Concurrency patterns](artifact/references/concurrency-patterns.md)
- [Full-text search](artifact/references/full-text-search.md)
- [Performance patterns](artifact/references/performance-patterns.md)
- [PostgreSQL operations](artifact/references/operations.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with SQL and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference guidance; not an automated database operator.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
