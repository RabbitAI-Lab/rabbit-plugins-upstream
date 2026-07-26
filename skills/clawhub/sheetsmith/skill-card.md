## Description: <br>
Sheetsmith helps agents inspect, summarize, filter, transform, and convert CSV, TSV, and Excel files with a pandas-based CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Sheetsmith to inspect spreadsheet structure, compute summaries, apply filters and column transformations, and export cleaned data without writing custom pandas code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet operations can read and write local files, and in-place edits can overwrite source data. <br>
Mitigation: Keep backups of important files, prefer writing to a new output path, and use in-place mode only when explicitly intended. <br>
Risk: Spreadsheet previews and exported files can include sensitive or private data from the source workbook. <br>
Mitigation: Review results before sharing them externally and only share spreadsheet outputs when explicitly requested. <br>


## Reference(s): <br>
- [Sheetsmith usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands] <br>
**Output Format:** [Markdown previews and local CSV, TSV, or XLSX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes modified data only when an output path or in-place mode is explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
