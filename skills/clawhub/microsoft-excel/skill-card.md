## Description: <br>
Microsoft Excel API integration with managed OAuth for reading and writing Excel workbooks, worksheets, ranges, tables, and charts stored in OneDrive or SharePoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Microsoft Excel data through Maton-managed OAuth, including workbook discovery, worksheet and range reads, table changes, chart creation, and other Excel operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes Microsoft Excel access through Maton and requires a MATON_API_KEY. <br>
Mitigation: Use the API key only in controlled environments and install the skill only after confirming the user trusts Maton to proxy Microsoft Excel access. <br>
Risk: Write and delete operations can alter workbook, worksheet, range, table, or chart data. <br>
Mitigation: Require explicit user approval before create, update, or delete calls, including confirmation of the target workbook, worksheet, and intended effect. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-excel) <br>
- [Publisher Profile](https://clawhub.ai/user/byungkyu) <br>
- [Microsoft Graph Excel API Overview](https://learn.microsoft.com/en-us/graph/api/resources/excel) <br>
- [Working with Excel in Microsoft Graph](https://learn.microsoft.com/en-us/graph/excel-concept-overview) <br>
- [Excel Workbook Resource](https://learn.microsoft.com/en-us/graph/api/resources/workbook) <br>
- [Excel Worksheet Resource](https://learn.microsoft.com/en-us/graph/api/resources/worksheet) <br>
- [Excel Range Resource](https://learn.microsoft.com/en-us/graph/api/resources/range) <br>
- [Excel Table Resource](https://learn.microsoft.com/en-us/graph/api/resources/table) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with REST endpoints and Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and network access; write operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
