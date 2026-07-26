## Description: <br>
Complete Excel workflow with local file processing, Google Drive sync, formula preservation, SQLite tracking, querying, and cell updates for .xlsx files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to process uploaded Excel workbooks, query workbook data, update cells or formulas, sync files to Google Drive, and track workbook metadata locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheets may be uploaded to Google Drive and tracked locally without clear opt-in, retention, or deletion controls. <br>
Mitigation: Use the skill only with workbooks approved for cloud backup; confirm upload behavior before processing, constrain Google Drive permissions, and document how Drive copies and local tracker records are deleted. <br>
Risk: Workbook updates can modify and re-upload files, which may overwrite important spreadsheet data or formulas. <br>
Mitigation: Keep backups before updates, review proposed cell and formula changes, and verify results in Excel or a compatible spreadsheet tool after processing. <br>
Risk: Confidential, regulated, client, or financial workbooks may be exposed through cloud sync or local tracking. <br>
Mitigation: Avoid sensitive workbooks unless policy permits the configured Google Drive account and local storage path; use restricted accounts and remove copies after use. <br>


## Reference(s): <br>
- [Excel Workflow ClawHub Page](https://clawhub.ai/legionspace-hackathon/skills/excel-workflow) <br>
- [openpyxl Documentation](https://openpyxl.readthedocs.io/) <br>
- [rclone Documentation](https://rclone.org/docs/) <br>
- [Google Drive with rclone](https://rclone.org/drive/) <br>
- [Microsoft Excel .xlsx File Format](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file operations, Google Drive sync commands, SQLite tracking, and workbook cell updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, artifact metadata, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
