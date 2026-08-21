## Description:

福昕 Office 表格助编 helps an agent automate common Fuxin Office Excel workbook tasks, including extracting data into new sheets, applying conditional formatting, and creating charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users who work in Fuxin Office Excel can use this skill to ask an agent to extract spreadsheet data, highlight matching cells, and generate charts while preserving review points for workbook changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read from and modify the active Excel workbook.

Mitigation: Review requests before execution, verify the active workbook during precheck, and confirm save operations only when the file should be written to disk.

Risk: Broad Excel triggers may invoke the skill from generic spreadsheet mentions.

Mitigation: Confirm the intended scenario and clarify missing ranges, target sheets, rules, or chart inputs before any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-excel)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with JSON MCP tool-call parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can propose or execute workbook read/write actions through Fuxin Office Excel; save operations require explicit user confirmation.]

## Skill Version(s):

1.00.03.195 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
