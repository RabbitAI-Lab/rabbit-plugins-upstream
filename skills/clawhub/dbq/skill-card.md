## Description: <br>
DBQ is a multi-database SQL assistant for querying MySQL, PostgreSQL, SQLite, and MariaDB across dev, test, and prod environments with read-only defaults, DML/DDL gating, and EXPLAIN analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yinpengfei](https://clawhub.ai/user/yinpengfei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding agents use this skill to run database queries, inspect schema, test connections, preview write operations, and manage SQL across dev, test, and prod database aliases without exposing raw connection details in prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can run write or schema-changing SQL when a database alias permits DML or DDL. <br>
Mitigation: Use least-privilege database accounts, keep production aliases read-only by default, and require human review for DML or DDL before execution. <br>
Risk: DB_QUERY_ASSUME_YES=1 can bypass interactive confirmation for write operations. <br>
Mitigation: Do not enable DB_QUERY_ASSUME_YES=1 for production workflows; use --dry-run and explicit approval before writes. <br>
Risk: Local credentials or sensitive query values can be exposed through credential retrieval or SQL logs. <br>
Mitigation: Avoid --keychain-get, do not read local connection or .env files into agent context, and review local SQL logs for sensitive values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yinpengfei/skills/dbq) <br>
- [Database driver installation guide](references/drivers.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell commands; command output may be table text, JSON, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local database aliases and environment selection; SQL results and logs may contain sensitive database values.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
