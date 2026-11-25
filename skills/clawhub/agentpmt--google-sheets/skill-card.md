## Description:

Google Sheets: Work with Google Sheets using safe short actions: discover tabs and headers, read values with exact one-based row numbers, append rows and columns, update selected fields, write or clear exact cell ranges, archive. Use when an agent needs google sheets, google sheets api, append spreadsheet rows safely, update crm style rows by key, export a sheet to csv or pdf, create reporting spreadsheets, add conditional formatting, spreadsheet id through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Agents connected to AgentPMT use this skill to create, read, update, format, share, and export Google Sheets through short actions with explicit row and range guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates this release suspicious with medium confidence and reports unpinned commands that install other skills; coverage is partial because local references are missing.

Mitigation: Review the referenced setup guidance and verify the installer and downloaded skill versions before installing or relying on them.

Risk: The spreadsheet sharing action can change access or ownership beyond the stated scope.

Mitigation: Before sharing, confirm the spreadsheet, intended recipient or audience, and least-privilege role; verify the resulting access.

## Reference(s):

- [Google Sheets on ClawHub](https://clawhub.ai/agentpmt/skills/google-sheets)
- [AgentPMT Google Sheets API marketplace](https://www.agentpmt.com/marketplace/google-sheets-api)
- [AgentPMT account MCP and REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What is AgentPMT](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Spreadsheet data, Export files]

**Output Format:** [AgentPMT action requests and responses; spreadsheet exports may be CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions operate on the connected account's spreadsheets; exports are stored in AgentPMT File Manager.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
