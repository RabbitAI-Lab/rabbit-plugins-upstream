## Description: <br>
OpenClaw skill that installs a Google Sheets CLI with setup steps and commands for read/write, batch, formatting, and sheet management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to configure and run a service-account Google Sheets CLI for repeatable read/write, batch, formatting, and sheet-management workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured service-account credentials allow the skill to read and change spreadsheets shared with that account. <br>
Mitigation: Share only required spreadsheets with the service account, prefer read-only scope for read workflows, and test write or destructive commands on noncritical spreadsheets first. <br>
Risk: Service-account key material can be exposed through committed files, logs, or inline shell history. <br>
Mitigation: Keep service-account keys private, avoid inline secrets in shell commands, and do not commit credential files. <br>
Risk: Sheet-management and batch commands can clear ranges, change formatting, rename sheets, or delete sheets. <br>
Mitigation: Review command arguments and JSON request bodies before execution, especially for clear, deleteSheet, batch, and formatting operations. <br>


## Reference(s): <br>
- [Google Sheets API Field Guide](assets/sheets-api-guide.md) <br>
- [Google Sheets API usage limits](https://developers.google.com/workspace/sheets/api/limits) <br>
- [spreadsheets.values.append reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append) <br>
- [ValueInputOption reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption) <br>
- [spreadsheets.batchUpdate reference](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) <br>
- [Google Sheets API batch requests guide](https://developers.google.com/workspace/sheets/api/guides/batch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and CLI JSON output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The installed CLI writes JSON to stdout and exits non-zero on errors.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
