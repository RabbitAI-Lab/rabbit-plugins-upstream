## Description: <br>
OpenClaw skill that installs a Google Sheets CLI with setup steps and commands for read/write, batch, formatting, and sheet management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to configure and run a service-account-backed Google Sheets CLI for repeatable spreadsheet reads, writes, batch updates, formatting, and sheet management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Google service-account key to access spreadsheets shared with that account. <br>
Mitigation: Use a dedicated least-privilege service account, share only the spreadsheets needed for the workflow, and keep the key out of the repository. <br>
Risk: Write, clear, deleteSheet, batchWrite, and raw batch commands can change or remove spreadsheet data. <br>
Mitigation: Review destructive or bulk update commands before execution and prefer read-only scope for read workflows. <br>


## Reference(s): <br>
- [Google Sheets API Field Guide](assets/sheets-api-guide.md) <br>
- [Google Sheets API Usage Limits](https://developers.google.com/workspace/sheets/api/limits) <br>
- [spreadsheets.values.append Reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append) <br>
- [ValueInputOption Reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption) <br>
- [spreadsheets.batchUpdate Reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) <br>
- [Google Sheets Batch Requests Guide](https://developers.google.com/workspace/sheets/api/guides/batch) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash examples and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes JSON to stdout and returns a non-zero exit code on errors.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
