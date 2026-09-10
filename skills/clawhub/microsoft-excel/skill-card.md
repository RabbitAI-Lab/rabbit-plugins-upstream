## Description:

Microsoft Excel API integration with managed OAuth for reading and writing Excel workbooks, worksheets, ranges, tables, and charts stored in OneDrive or SharePoint through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and modify Excel files in connected Microsoft accounts, including workbook metadata, worksheets, ranges, tables, rows, columns, named items, and charts. It is suited to spreadsheet automation where OAuth-backed access, explicit user approval for writes, and least-privilege connection handling are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Microsoft Excel account access through the third-party Maton gateway and its CLI or SDK packages.

Mitigation: Install and use it only when the user trusts Maton for the connected Excel account, and consider pinning or verifying Maton package versions in controlled environments.

Risk: OAuth grants or API keys can expose spreadsheet data if over-broad, stale, printed, or stored insecurely.

Mitigation: Prefer OAuth over API keys, approve only the intended Excel connection and scopes, never print or persist credentials, and revoke unused connections.

Risk: Write operations can alter or delete workbook data, worksheets, ranges, tables, rows, columns, and charts.

Mitigation: Default to read/list calls, verify target identifiers and account context first, and require explicit user approval for every POST, PUT, PATCH, or DELETE operation.

Risk: Content returned from spreadsheets or API responses may contain untrusted instructions or data.

Mitigation: Treat returned content as data, do not execute or interpolate it into shell commands, and do not let it choose follow-up endpoints or recipients.

## Reference(s):

- [ClawHub Microsoft Excel Skill](https://clawhub.ai/byungkyu/skills/microsoft-excel)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Graph Excel API Overview](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- [Working with Excel in Microsoft Graph](https://learn.microsoft.com/en-us/graph/excel-concept-overview)
- [Excel Workbook Resource](https://learn.microsoft.com/en-us/graph/api/resources/workbook)
- [Excel Worksheet Resource](https://learn.microsoft.com/en-us/graph/api/resources/worksheet)
- [Excel Range Resource](https://learn.microsoft.com/en-us/graph/api/resources/range)
- [Excel Table Resource](https://learn.microsoft.com/en-us/graph/api/resources/table)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI or SDK calls to Microsoft Graph Excel endpoints and should default to read/list operations before any write.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
