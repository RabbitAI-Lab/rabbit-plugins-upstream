## Description: <br>
Db Explorer helps agents connect to PostgreSQL, MySQL, SQLite, MongoDB, and Redis databases to inspect schemas, run queries, diagnose issues, and export data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lrg913427-dot](https://clawhub.ai/user/lrg913427-dot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they need an agent to explore database structure, run bounded diagnostic queries, export selected data, or prepare database backup, restore, and migration commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce commands that export, import, restore, or migrate real database data. <br>
Mitigation: Review exact commands before execution, confirm the target database, prefer staging first, and take a backup before restore, import, migration, or full-table export work. <br>
Risk: Database credentials and generated dumps or exports may expose sensitive data. <br>
Mitigation: Use environment variables or secret managers for credentials, avoid echoing passwords, keep exports in controlled locations, and delete temporary files when no longer needed. <br>
Risk: Unbounded queries or full exports can be slow, expensive, or disruptive on production systems. <br>
Mitigation: Use read-only access by default, add result limits unless explicitly approved, and run high-impact operations only after confirming scope and timing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lrg913427-dot/skills/db-explorer) <br>
- [Publisher profile](https://clawhub.ai/user/lrg913427-dot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell and SQL command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include database connection guidance, schema summaries, query examples, export commands, and safety checks for destructive or large operations.] <br>

## Skill Version(s): <br>
2.5.2 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
