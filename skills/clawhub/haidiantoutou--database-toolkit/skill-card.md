## Description: <br>
Execute SQL queries, update records, analyze data, and perform backup and restore on local SQLite and remote MySQL databases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data analysts use this skill to query, update, inspect, back up, import, and export data in SQLite and MySQL databases during application and data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute SQL that changes or deletes database data. <br>
Mitigation: Use read-only credentials for exploration, review SQL before execution, and back up important databases before writes or deletes. <br>
Risk: Backup and export workflows can expose sensitive table data. <br>
Mitigation: Avoid exporting sensitive tables unless the destination is controlled, and mask or omit sensitive fields when sharing outputs. <br>
Risk: Remote database access can concentrate privileges in agent-managed credentials. <br>
Mitigation: Use least-privileged accounts, rotate credentials regularly, and avoid embedding production secrets in reusable examples or configuration. <br>


## Reference(s): <br>
- [Database Toolkit ClawHub page](https://clawhub.ai/haidiantoutou/skills/database-toolkit) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples, SQL snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include database connection settings, SQL examples, backup/export paths, and dependency notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
