## Description:

Lite Sqlite helps OpenClaw agents create and manage lightweight local SQLite databases for efficient persistence, memo storage, caching, and small-scale application data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[omprasad122007-rgb](https://clawhub.ai/user/omprasad122007-rgb)

### License/Terms of Use:


## Use Case:

Developers and agent builders use Lite Sqlite to add local SQLite persistence, memo and session storage, caching, and database maintenance workflows to OpenClaw agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable an agent to create, alter, delete, optimize, copy, restore, and replace local SQLite databases it can access.

Mitigation: Review proposed SQL, table names, WHERE clauses, target paths, and destructive operations before execution; take backups before delete, update, migration, restore, or replace-import workflows.

Risk: Weak safeguards around arbitrary SQL and schema operations can affect sensitive or production databases.

Mitigation: Restrict use to approved local databases and avoid production or sensitive data unless an explicit human review approves the command plan.

## Reference(s):

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [DuckDB Documentation](https://duckdb.org/docs/)
- [SQLite Query Optimizer Overview](https://www.sqlite.org/optoverview.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated database changes depend on the target database path and commands the agent runs.]

## Skill Version(s):

1.0.0 (source: server release metadata, created 2026-02-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
