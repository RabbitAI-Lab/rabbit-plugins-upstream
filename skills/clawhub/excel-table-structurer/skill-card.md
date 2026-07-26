## Description: <br>
Structures hierarchical Excel (.xlsx) tables by handling parent-child relationships, fill-down values, group-header display, and filter-friendly formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and spreadsheet users use this skill to restructure hierarchical Excel workbooks such as test-case sheets, project task lists, and ledger detail tables. It helps analyze column roles, build a JSON column specification, run the restructuring script, and return a formatted workbook. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet files can contain sensitive business data. <br>
Mitigation: Use the skill only with files the agent is authorized to process, and handle transformed workbooks according to the same data-access rules as the originals. <br>
Risk: An incorrect column specification or output path can produce an unusable workbook or overwrite an unintended file. <br>
Mitigation: Review the JSON specification and output path before running the script, then inspect the generated workbook before sharing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/excel-table-structurer) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [XLSX workbook plus JSON summary and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads a provided .xlsx file and writes a transformed workbook to the requested output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
