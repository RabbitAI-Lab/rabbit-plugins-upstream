## Description:

This skill helps agents create, modify, and organize Flydb migration SQL scripts and related migration-directory configuration while following Flydb naming, versioning, checksum, undo, repeatable migration, and error-handling rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database maintainers use this skill to plan and author Flydb migration files, choose V/R/U naming and version patterns, resolve migration-directory errors, and prepare validation or dry-run commands without running database-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated migration SQL can later change database schema or data when applied.

Mitigation: Review generated SQL and run Flydb validate plus dry-run migrate checks before applying migrations.

Risk: Changing an already-applied versioned migration can cause checksum validation failures and inconsistent environments.

Mitigation: Carry historical changes in a new versioned migration and use repair only after explicit user review and confirmation.

Risk: Repeatable migrations rerun when their checksum changes.

Mitigation: Confirm repeatable migration scripts are idempotent or safely rebuildable before modifying them.

Risk: Flydb placeholder syntax can conflict with application templates that also use ${...} variables.

Mitigation: Use placeholder-replacement=false when template variables must be stored literally, and validate the resulting migration behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zzxcoding/skills/flydb-migration-scripts)
- [Publisher Profile](https://clawhub.ai/user/zzxcoding)
- [Naming and Versions](references/naming-and-versions.md)
- [Errors and Discipline](references/errors-and-discipline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with SQL snippets, shell commands, configuration examples, and file path lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Flydb migration SQL files and flydb.locations configuration edits when the user authorizes file changes; does not execute database-changing commands.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
