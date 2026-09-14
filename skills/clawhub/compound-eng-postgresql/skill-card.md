## Description:

Provides PostgreSQL guidance for schema design, query optimization, indexing, administration, JSONB, partitioning, RLS, CTEs, window functions, and EXPLAIN ANALYZE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to design PostgreSQL schemas, tune queries and indexes, plan migrations, and review operational or security-sensitive database patterns such as RLS and concurrency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RLS identity-context and SECURITY DEFINER patterns may be unsafe if applied directly and could weaken database access controls.

Mitigation: Require trusted identity handling, transaction scoping, restricted grants, fixed search_path, least-privilege ownership, and negative access-control tests before relying on the skill for RLS work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-postgresql)
- [Schema and migrations](references/schema-and-migrations.md)
- [Query and index patterns](references/query-and-index-patterns.md)
- [Security and operations](references/security-and-operations.md)
- [Operations](references/operations.md)
- [Concurrency patterns](references/concurrency-patterns.md)
- [Full-text search](references/full-text-search.md)
- [Performance patterns](references/performance-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with SQL and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PostgreSQL SQL snippets, migration patterns, query-plan review steps, and operational checklists.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
