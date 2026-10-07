## Description:

Provides PostgreSQL guidance for schema design, query optimization, indexing, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to design PostgreSQL schemas, tune queries and indexes, plan migrations, and review database operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying suggested migrations or index drops can lock tables or cause data loss.

Mitigation: Review SQL, test against representative data, and stage changes with rollback and lock budgets.

Risk: Misconfigured row-level security or backup settings can expose data or hinder recovery.

Mitigation: Review policies against tenant boundaries and verify backups with restore tests before production use.

Risk: Full-text search configuration may not match the data's language or locale.

Mitigation: Validate language settings and search results against representative content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)
- [Schema and migrations](artifact/references/schema-and-migrations.md)
- [Query and index patterns](artifact/references/query-and-index-patterns.md)
- [Security and operations](artifact/references/security-and-operations.md)
- [Concurrency patterns](artifact/references/concurrency-patterns.md)
- [Performance patterns](artifact/references/performance-patterns.md)
- [Full-text search](artifact/references/full-text-search.md)
- [Operations](artifact/references/operations.md)

## Skill Output:

**Output Type(s):** [Guidance, SQL, Shell commands, Configuration instructions]

**Output Format:** [Markdown with SQL and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated SQL before applying it to real databases.]

## Skill Version(s):

5.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
