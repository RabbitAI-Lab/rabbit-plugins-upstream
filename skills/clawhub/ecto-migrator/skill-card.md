## Description: <br>
Generate Ecto migrations from natural language or schema descriptions. Handles tables, columns, indexes, constraints, references, enums, and partitioning. Supports reversible migrations, data migrations, and multi-tenant patterns. Use when creating or modifying database schemas, adding indexes, altering tables, creating enums, or performing data migrations in an Elixir project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to draft Ecto database migrations for Elixir applications from natural language or schema-change descriptions, including tables, columns, indexes, constraints, references, enums, partitioning, and data migrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated migration drafts may include destructive schema changes, raw SQL, cascading deletes, extension changes, production index operations, or data backfills that affect application data. <br>
Mitigation: Review every generated migration before running it, with special attention to raw SQL, drops or removals, cascading deletes, data backfills, PostgreSQL extensions, and production index changes. <br>
Risk: Database migrations can lock tables or fail on large production datasets if index and data-change strategies are not checked. <br>
Mitigation: Use the skill's production guidance for separate concurrent index migrations and separate data migrations, then validate the final migration against the target database and deployment process. <br>


## Reference(s): <br>
- [Column Types Reference](references/column-types.md) <br>
- [Index Patterns Reference](references/index-patterns.md) <br>
- [ClawHub skill page](https://clawhub.ai/gchapim/skills/ecto-migrator) <br>
- [Publisher profile](https://clawhub.ai/user/gchapim) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Elixir, SQL, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory migration drafts and review checklists; they do not execute database changes automatically.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
