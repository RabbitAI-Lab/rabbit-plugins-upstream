## Description: <br>
Use when designing database schemas, writing migrations, optimizing SQL queries, fixing N+1 problems, creating indexes, setting up PostgreSQL, configuring EF Core, implementing caching, partitioning tables, or any database performance question. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jgarrison929](https://clawhub.ai/user/jgarrison929) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill for database schema design, migration planning, SQL query tuning, PostgreSQL operations, EF Core migration workflows, indexing, caching, partitioning, and performance troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SQL, migrations, and schema changes can alter or delete production data if applied without review. <br>
Mitigation: Review generated SQL, test migrations in a non-production environment, and confirm rollback steps before execution. <br>
Risk: Audit logging examples may copy sensitive fields into JSON audit records. <br>
Mitigation: Exclude, redact, or encrypt sensitive fields before enabling audit logging in an application database. <br>
Risk: Caching and materialized-view guidance can return stale data when invalidation or refresh behavior is incomplete. <br>
Mitigation: Define cache invalidation, TTL, and materialized-view refresh policies that match the application's data consistency requirements. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with SQL, shell, C#, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only guidance; generated SQL and migration commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
