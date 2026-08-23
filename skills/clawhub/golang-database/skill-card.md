## Description:

Comprehensive guide for Go database access: parameterized queries, struct scanning, NULLable columns, transactions, isolation levels, SELECT FOR UPDATE, connection pools, batch processing, context propagation, and migration tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill when writing, reviewing, or debugging Go code that interacts with PostgreSQL, MariaDB, MySQL, or SQLite. It helps agents produce database access guidance, Go code patterns, review findings, and testing recommendations while avoiding schema generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated database code or review guidance may still contain incorrect SQL, unsafe transaction handling, or misleading assumptions about an application's data model.

Mitigation: Review generated Go and SQL changes, run unit and integration tests, and verify behavior against the target database before deployment.

Risk: Advice about migrations, indexes, schema design, or financial transactions can affect live data integrity and production performance.

Mitigation: Require human engineering review and staging validation before applying database migrations, DDL, index changes, or high-value transaction logic.

Risk: The skill can read and edit Go files and propose Go tooling commands when invoked in a repository.

Mitigation: Use it in the intended Go workspace, inspect diffs and commands before applying them, and avoid connecting tests or commands to production databases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-database)
- [ClawHub publisher profile](https://clawhub.ai/user/samber)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Transactions](references/transactions.md)
- [Testing Database Code](references/testing.md)
- [Database Performance](references/performance.md)
- [Struct Scanning and NULLable Columns](references/scanning.md)
- [database/sql tutorial](https://go.dev/doc/database/)
- [sqlx](https://github.com/jmoiron/sqlx)
- [pgx](https://github.com/jackc/pgx)
- [golang-migrate](https://github.com/golang-migrate/migrate)
- [Flyway](https://flywaydb.org/)
- [Atlas](https://atlasgo.io/)
- [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Go, SQL, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review findings, repository code changes, database testing patterns, and Go tooling commands.]

## Skill Version(s):

1.3.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
