## Description:

Convert natural language queries to KWDB SQL for time series data, relational data, and cross-model analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to translate natural-language requests into KWDB-specific SQL for IoT time-series, relational, and cross-model database work. It supports schema-aware query generation, SQL formatting, and optional execution through kwdb-mcp-server when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SQL can include broad write or administrative statements against a live KWDB database.

Mitigation: Use read-only database credentials by default, enable write-query only in trusted sessions, and review every DELETE, DROP, ALTER, UPDATE, INSERT, or CREATE statement before execution.

Risk: When kwdb-mcp-server is unavailable, generated SQL may rely on assumed table or column names.

Mitigation: Require the response to mark assumed schema clearly and have the user verify table names, columns, time ranges, and LIMIT clauses before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kwdb/skills/kwdb-text2sql-aiot)
- [Output Template](assets/output-template.md)
- [Query Scenarios](references/scenarios.md)
- [KWDB MCP Server Integration](references/mcp-integration.md)
- [Time Series DDL Reference](references/ts-ddl.md)
- [Time Series Downsampling](references/ts-downsampling.md)
- [Time Series Interpolation](references/ts-interpolation.md)
- [Time Series Latest Value](references/ts-latest-value.md)
- [Window Functions and Event Detection](references/ts-window-events.md)
- [Relational Query Reference](references/relational.md)
- [Cross-Model Query Reference](references/cross-model.md)
- [KWDB Functions Quick Reference](references/ts-functions.md)
- [KWDB Relational Functions Reference](references/relational-functions.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with SQL code blocks, assumptions, field mappings, validation checklists, and optional execution results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include schema verification status, generated KWDB SQL, read or write execution results, and user-facing warnings when schema is assumed.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
