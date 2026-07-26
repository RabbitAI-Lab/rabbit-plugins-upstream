## Description: <br>
Queries databases through the Archery SQL platform, including SQL execution, schema exploration, table listing, and duplicate-data analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ming1007520388](https://clawhub.ai/user/ming1007520388) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and database operators with approved Archery access use this skill to run SQL queries, inspect database and table structure, search tables and fields, and prepare duplicate-record cleanup artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad database-query capability could expose sensitive data or affect production systems if used with an over-privileged Archery account. <br>
Mitigation: Use a least-privilege, preferably read-only Archery user, avoid production unless explicitly approved, and review SQL before execution. <br>
Risk: Saved credentials and session cookies can grant Archery access if exposed. <br>
Mitigation: Protect ~/.archery/config.json and ~/.archery/cache/session.json, restrict file permissions, and do not paste cookie output into chats, logs, or tickets. <br>
Risk: The duplicate-data workflow can generate DELETE statements that may remove records if run without review. <br>
Mitigation: Use analysis-only mode when possible, inspect generated SQL, and run cleanup statements only after database-owner approval and backup checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ming1007520388/skills/archery-sql-query) <br>
- [Configuration example](artifact/references/config-example.md) <br>
- [Supported database types](artifact/references/database-types.md) <br>
- [Table structure guide](artifact/references/table-structure-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, table or JSON query output, CSV duplicate reports, and generated SQL files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Archery credentials and cached sessions under ~/.archery; query output defaults to a limited row count unless changed by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
