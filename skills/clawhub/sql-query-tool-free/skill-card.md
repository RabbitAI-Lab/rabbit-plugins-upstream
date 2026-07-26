## Description: <br>
SQL查询工具(免费版) helps independent developers, operations teams, and AI agents run command-line SQL workflows across SQLite, PostgreSQL, MySQL, and SQL Server, including parameterized queries, execution-plan analysis, imports and exports, and portability checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to connect to relational databases from the command line, run parameterized queries, inspect execution plans, and handle basic import/export or migration assessment tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad database read, write, and delete actions, including production connections. <br>
Mitigation: Use read-only or least-privilege credentials by default; require explicit confirmation, backups, and a rollback plan before writes, deletes, resets, imports, exports, or production use. <br>
Risk: SQL or CLI guidance may be incorrect for the target database dialect, data shape, or execution context. <br>
Mitigation: Review generated SQL and commands before execution, test them in a non-production environment first, and inspect execution plans before applying changes to important data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sql-query-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with SQL, Python, shell-command examples, and JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose database CLI commands and SQL statements; require explicit confirmation for writes, deletes, resets, imports, exports, and production connections.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
