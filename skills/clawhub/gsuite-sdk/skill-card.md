## Description:

Helps agents use the gsuite-sdk Python library and CLI to read and manage Gmail, Calendar, Drive, Sheets, Tasks, and Contacts data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access and update Google Workspace email, events, files, spreadsheets, tasks, and contacts through the CLI or Python SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change real Gmail, Drive, Calendar, Sheets, Tasks, and Contacts data.

Mitigation: Use only accounts intended for automation, grant least-privilege OAuth scopes, and confirm before sending email, sharing files, changing records, or deleting data.

Risk: Exposed OAuth credentials or saved tokens could permit unauthorized account access.

Mitigation: Keep credentials.json, tokens.db, and exported tokens private.

Risk: Unpinned package installs may change between deployments.

Mitigation: Pin package versions for repeatable installs.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [Gmail usage](references/gmail.md)
- [Calendar usage](references/calendar.md)
- [Drive usage](references/drive.md)
- [Sheets usage](references/sheets.md)
- [Tasks and Contacts usage](references/tasks-contacts.md)
- [MCP server usage](references/mcp.md)
- [REST API and deployment](references/rest-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and Python examples; CLI results can be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google OAuth credentials and appropriate scopes are required.]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
