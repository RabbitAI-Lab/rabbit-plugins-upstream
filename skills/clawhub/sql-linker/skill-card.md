## Description: <br>
sql-linker helps agents query, insert, update, delete, audit, and bootstrap configured MySQL, PostgreSQL, or SQLite databases when a target table and approximate schema are known. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cloudcode-hans](https://clawhub.ai/user/cloudcode-hans) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to perform agent-assisted CRUD operations, inspect audit logs, and bootstrap database configuration for known tables in configured MySQL, PostgreSQL, or SQLite databases. For production environments with stronger credential isolation, the artifact recommends sql-linker-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-assisted CRUD can change or delete database records. <br>
Mitigation: Install only for databases where this behavior is acceptable, use a least-privileged database account, and keep read_only enabled until writes are needed. <br>
Risk: Database credentials may be recoverable if local configuration and encrypted environment values are both accessible. <br>
Mitigation: Keep dbpw_key secret, enable explicit credential approval for sensitive environments, and avoid plaintext passwords in configuration. <br>
Risk: Generated set_env scripts can persist environment variables in the user shell profile. <br>
Mitigation: Review any generated set_env script before running it. <br>
Risk: Audit records contain operator metadata and masked SQL in the target database. <br>
Mitigation: Treat sql_audit_log as sensitive operational data and manage retention and access controls in the target database. <br>


## Reference(s): <br>
- [sql-linker ClawHub page](https://clawhub.ai/cloudcode-hans/skills/sql-linker) <br>
- [sql-linker-cli production alternative](https://clawhub.ai/cloudcode-hans/skills/sql-linker-cli) <br>
- [cloudcode-hans publisher profile](https://clawhub.ai/user/cloudcode-hans) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and structured database operation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local ~/.sql_linker configuration files and write database audit records when invoked.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
