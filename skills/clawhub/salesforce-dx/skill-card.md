## Description: <br>
Query Salesforce data and manage sales pipelines using the `sf` CLI for SOQL queries, opportunity analysis, forecasts, exports, schema exploration, and CRM operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rjmcgirr-pl](https://clawhub.ai/user/rjmcgirr-pl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, revenue operators, and sales teams use this skill to inspect Salesforce schemas, run SOQL queries, analyze pipeline and forecast data, export CRM data, and prepare account or opportunity workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an authenticated Salesforce CLI session to read, export, import, or modify sensitive CRM records. <br>
Mitigation: Verify the target org before each run, prefer a sandbox or least-privilege Salesforce account, and require explicit approval before exports, imports, bulk upserts, or record-changing commands. <br>
Risk: Pipeline exports and query results may contain confidential contact details, account notes, opportunity descriptions, or forecast data. <br>
Mitigation: Treat generated files and query output as confidential business data and review sharing or storage decisions before use. <br>


## Reference(s): <br>
- [Advanced SOQL Patterns](references/soql-patterns.md) <br>
- [Pipeline & Forecast Queries](references/pipeline-queries.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and SOQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Salesforce CLI commands that query, export, import, or modify CRM data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
