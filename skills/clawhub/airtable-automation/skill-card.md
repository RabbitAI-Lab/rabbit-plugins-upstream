## Description: <br>
Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to guide agents through Airtable automation workflows, including records, bases, tables, fields, views, comments, formulas, pagination, and schema discovery through Rube MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting Rube MCP to Airtable can give the agent access to the user's Airtable workspace. <br>
Mitigation: Install only when that access is acceptable, use the least-privileged Airtable connection available, and test first on a non-production base when possible. <br>
Risk: Delete, update-table, create-field, and update-field actions can remove records or change Airtable schemas. <br>
Mitigation: Require the agent to show the exact base, table, record IDs, fields, and schema changes, then wait for explicit approval before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/airtable-automation) <br>
- [Publisher profile](https://clawhub.ai/user/sohamganatra) <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, API Calls] <br>
**Output Format:** [Markdown guidance with MCP setup steps, Airtable tool sequences, parameter notes, formulas, and workflow cautions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active Airtable connection; destructive and schema-changing workflows should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
