## Description:

Microsoft Excel API integration with managed OAuth for reading and writing Excel workbooks, worksheets, ranges, tables, and charts stored in OneDrive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect, read, and modify Microsoft Excel spreadsheets through Maton-managed OAuth access. It is intended for workbook, worksheet, range, table, chart, and cell-value workflows where writes and new connections require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Microsoft Excel, OneDrive, or SharePoint through Maton can grant access to spreadsheet data under the selected OAuth scopes.

Mitigation: Review requested OAuth scopes, prefer read-only access when possible, and connect only the account needed for the task.

Risk: Write, delete, or connection-creation operations can modify spreadsheet data or account access.

Mitigation: Require explicit user confirmation before creating a connection or executing POST, PUT, PATCH, or DELETE requests, and confirm the target resource and intended effect.

Risk: Long-lived API keys or returned provider tokens can leak if printed, logged, stored, or passed through shell history.

Mitigation: Use OAuth through the Maton CLI when available, keep credentials in the operating system credential store, and never print, persist, or pass secrets on the command line.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-excel)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Graph Excel API Overview](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- [Working with Excel in Microsoft Graph](https://learn.microsoft.com/en-us/graph/excel-concept-overview)
- [Excel Workbook Resource](https://learn.microsoft.com/en-us/graph/api/resources/workbook)
- [Excel Worksheet Resource](https://learn.microsoft.com/en-us/graph/api/resources/worksheet)
- [Excel Range Resource](https://learn.microsoft.com/en-us/graph/api/resources/range)
- [Excel Table Resource](https://learn.microsoft.com/en-us/graph/api/resources/table)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, SDK snippets, API paths, request payloads, and safety guidance for Excel operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
