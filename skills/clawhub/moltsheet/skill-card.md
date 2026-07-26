## Description: <br>
Use the Moltsheet CLI to manage spreadsheet-style data for AI workflows, including creating sheets, inspecting schemas, importing rows, updating cells, sharing sheets, and running read-only SQL queries over accessible sheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youssefbm2008](https://clawhub.ai/user/youssefbm2008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access and manage Moltsheet spreadsheet data through the CLI, including filtered reads, selected columns, imports, mutations, sharing, and read-only SQL analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet writes, deletes, destructive schema changes, and collaborator sharing can change or expose Moltsheet data. <br>
Mitigation: Confirm the sheet ID, intended operation, recipient slug, and access level before allowing mutating or sharing commands. <br>
Risk: Sensitive spreadsheet data may be stored or shared through Moltsheet. <br>
Mitigation: Avoid using the skill with sensitive spreadsheets unless the user accepts storing and sharing that data through Moltsheet. <br>
Risk: Imports and cell updates can fail when schema, row IDs, column names, or batch sizes are wrong. <br>
Mitigation: Use --json, inspect error.code and error.action, correct schema or data issues, and verify results with sheet get or sheet list after writes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/youssefbm2008/skills/moltsheet) <br>
- [Moltsheet Service](https://www.moltsheet.com) <br>
- [Moltsheet API v1](https://www.moltsheet.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI responses are typically requested with --json; structured inputs are passed through files or stdin.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
