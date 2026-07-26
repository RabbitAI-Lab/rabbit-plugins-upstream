## Description: <br>
Google Sheets API integration with managed OAuth for reading and writing spreadsheet data, creating sheets, applying formatting, and managing ranges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Google Sheets through Maton-managed OAuth, including reading spreadsheet data, writing values, creating sheets, applying formatting, and managing ranges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Maton API key and access to connected Google Sheets accounts. <br>
Mitigation: Install only if you trust Maton with the connected account, store MATON_API_KEY as a secret, and avoid exposing it in terminal output, screenshots, logs, or support chats. <br>
Risk: Write, clear, delete, and batch update operations can change spreadsheet content or structure. <br>
Mitigation: Confirm spreadsheet IDs, ranges, connected accounts, and intended effects with the user before allowing mutating operations. <br>
Risk: Multiple Google account connections can route requests to an unintended account. <br>
Mitigation: Specify the intended Maton connection when multiple Google Sheets connections are active. <br>


## Reference(s): <br>
- [ClawHub Google Sheets skill page](https://clawhub.ai/byungkyu/skills/google-sheets) <br>
- [Maton website](https://maton.ai) <br>
- [Google Sheets API REST reference](https://developers.google.com/workspace/sheets/api/reference/rest) <br>
- [Google Sheets API spreadsheets.get](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/get) <br>
- [Google Sheets API spreadsheets.create](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/create) <br>
- [Google Sheets API spreadsheets.batchUpdate](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) <br>
- [Google Sheets API batchUpdate request types](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, HTTP endpoint examples, and Python or JavaScript code snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY, and an active Google Sheets OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
