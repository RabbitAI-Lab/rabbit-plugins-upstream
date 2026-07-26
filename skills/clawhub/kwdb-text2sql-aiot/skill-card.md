## Description: <br>
Convert natural language queries to KWDB SQL for time series data, relational data, and cross-model analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database users use this skill to convert natural-language requests into KWDB SQL for IoT time-series data, relational data, and cross-model analysis. When kwdb-mcp-server is available, it can discover schema and optionally execute approved SQL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SQL may query or modify a KWDB database when the user approves execution through kwdb-mcp-server. <br>
Mitigation: Review generated SQL before approval, especially CREATE, DROP, ALTER, INSERT, UPDATE, and DELETE statements. <br>
Risk: Schema assumptions can produce incorrect SQL when MCP schema discovery is unavailable. <br>
Mitigation: Confirm table names, column names, and time ranges, and treat assumed-schema output as needing verification. <br>


## Reference(s): <br>
- [KWDB Text2SQL AIoT ClawHub listing](https://clawhub.ai/kwdb/skills/kwdb-text2sql-aiot) <br>
- [Query Scenarios](references/scenarios.md) <br>
- [KWDB MCP Server Integration](references/mcp-integration.md) <br>
- [Time Series DDL Reference](references/ts-ddl.md) <br>
- [Time Series Downsampling](references/ts-downsampling.md) <br>
- [Time Series Interpolation](references/ts-interpolation.md) <br>
- [Time Series Latest Value](references/ts-latest-value.md) <br>
- [Window Functions and Event Detection](references/ts-window-events.md) <br>
- [Cross-Model Query Reference](references/cross-model.md) <br>
- [Relational Query Reference](references/relational.md) <br>
- [KWDB Functions Quick Reference](references/ts-functions.md) <br>
- [KWDB Relational Functions Reference](references/relational-functions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with SQL code blocks, assumptions, field mappings, validation checklists, and optional execution results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include schema verification status, generated KWDB SQL, and tabular query results when execution is approved.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
