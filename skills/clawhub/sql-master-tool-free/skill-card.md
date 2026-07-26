## Description: <br>
SQL大师工具(免费版) helps independent developers and AI agents design schemas, write queries, plan indexes, draft migration scripts, and perform backup and restore workflows for SQLite, PostgreSQL, and MySQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, database operators, DBAs, data analysts, and AI agents use this skill to create SQL schemas, queries, indexes, migration plans, and backup or restore command workflows for common relational database tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide high-impact database changes such as migrations, imports, restores, deletes, or updates without explicit production-safety controls. <br>
Mitigation: Require explicit confirmation before any database-changing action, use least-privilege credentials, default to development or test databases, and keep current backups before production changes. <br>
Risk: Generated SQL or command-line workflows may target the wrong database or run with excessive privileges. <br>
Mitigation: Review connection details, environment variables, and command targets before execution; prefer read-only or scoped credentials unless write access is required. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/sql-master-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with SQL snippets, shell command examples, and optional JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose database-changing commands; review credentials, target database, and backups before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
