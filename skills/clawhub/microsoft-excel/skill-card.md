## Description:

Microsoft Excel API integration with managed OAuth for reading and writing workbooks, worksheets, ranges, tables, and charts stored in OneDrive or SharePoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill to access or modify Excel spreadsheet data through authenticated Maton-managed Microsoft Graph calls. It supports worksheet, range, table, chart, connection, function, and trigger workflows when the user has approved the relevant account access and write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or modify Excel files available to the connected Microsoft account.

Mitigation: Use OAuth, scope connections narrowly, default to read and list operations, and require explicit user confirmation before creating connections or performing writes.

Risk: Hosted functions and triggers can create persistent automation over connected account data.

Mitigation: Create hosted functions or triggers only for a specific reviewed task, summarize least-privilege access before approval, and avoid broad trigger scopes.

Risk: API keys and raw responses can expose long-lived credentials or spreadsheet contents.

Mitigation: Prefer OAuth over API keys, avoid exporting MATON_API_KEY, store credentials only through the supported credential flow, and avoid logging full response bodies.

## Reference(s):

- [Microsoft Graph Excel API Overview](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- [Working with Excel in Microsoft Graph](https://learn.microsoft.com/en-us/graph/excel-concept-overview)
- [Excel Workbook Resource](https://learn.microsoft.com/en-us/graph/api/resources/workbook)
- [Excel Worksheet Resource](https://learn.microsoft.com/en-us/graph/api/resources/worksheet)
- [Excel Range Resource](https://learn.microsoft.com/en-us/graph/api/resources/range)
- [Excel Table Resource](https://learn.microsoft.com/en-us/graph/api/resources/table)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-excel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authenticated Maton commands and implementation guidance; API responses may contain user spreadsheet data.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
