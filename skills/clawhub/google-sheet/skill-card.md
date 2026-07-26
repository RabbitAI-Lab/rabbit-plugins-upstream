## Description: <br>
Read, write, append, clear, format, and manage Google Sheets through a Node.js CLI using the Google Sheets API and a Google Cloud service account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[longmaba](https://clawhub.ai/user/longmaba) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to inspect, update, format, and manage Google Sheets when a service account has been granted access to the target spreadsheets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, change, clear, or delete spreadsheet data that is shared with its service account. <br>
Mitigation: Use a dedicated service account, share only the spreadsheets it needs, and review spreadsheet IDs, ranges, and sheet names before write, clear, or deleteSheet commands. <br>
Risk: A service-account JSON key can expose access to shared spreadsheets if it is committed or placed in a shared location. <br>
Mitigation: Keep the key out of repositories and shared folders, restrict file permissions, and rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/longmaba/skills/google-sheet) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON] <br>
**Output Format:** [JSON command output with Markdown setup and usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses service-account credentials and Google Sheets API access for spreadsheets shared with that account.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
