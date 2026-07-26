## Description: <br>
Manages MaybeAI spreadsheet workflows for upload and import, workbook profiling, worksheet inspection, reads and writes, formulas, SQL result tables, lineage tracing, formatting, sharing, and export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external spreadsheet users use this skill to operate MaybeAI workbooks through guided API workflows, including importing, profiling, editing, verifying, sharing, and exporting spreadsheets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MaybeAI API token can authorize reading, modifying, deleting, exporting, and sharing spreadsheets. <br>
Mitigation: Use a token scoped to the intended workspace and avoid workbook profiling, export, or sharing on sensitive spreadsheets unless that data flow is intended. <br>
Risk: Example scripts include destructive spreadsheet operations such as delete, clear, and overwrite actions. <br>
Mitigation: Edit scripts before running them, test against copied workbooks, and export or back up important spreadsheets before destructive operations. <br>
Risk: Sharing examples can change spreadsheet visibility to public or grant editor access. <br>
Mitigation: Review visibility and permission payloads before execution and prefer private or viewer-only access unless public editor access is explicitly required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-skill) <br>
- [MaybeAI Uni Homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [File Management Reference](references/file-management.md) <br>
- [Read/Write Reference](references/read-write.md) <br>
- [Formulas and SQL Reference](references/formulas-sql.md) <br>
- [Workbook Profile Reference](references/workbook-profile.md) <br>
- [Formula Lineage Trace Reference](references/lineage-trace.md) <br>
- [Permission And Sharing Reference](references/permission-sharing.md) <br>
- [Errors and Recovery Reference](references/errors-recovery.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and includes verification steps after spreadsheet writes.] <br>

## Skill Version(s): <br>
0.13.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
