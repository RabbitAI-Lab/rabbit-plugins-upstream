## Description:

Helps agents use the gsuite-sdk CLI and Python library to work with Gmail, Calendar, Drive, Sheets, Tasks, and Contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and manage Google Workspace mail, calendars, files, spreadsheets, tasks, and contacts through CLI commands or Python code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Google Workspace access can expose private mail, files, and contacts.

Mitigation: Grant only necessary OAuth scopes and keep credential and token files private.

Risk: Sending email, sharing files, editing calendars or spreadsheets, and deleting data can have unintended effects.

Mitigation: Require user confirmation before consequential write or sharing actions.

Risk: An exposed REST server or disabled API-key check could allow unauthorized access.

Mitigation: Restrict server access and do not disable API-key checks without another strong access control.

Risk: Unpinned dependencies can change behavior in managed deployments.

Mitigation: Pin package versions in managed environments.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [Gmail reference](references/gmail.md)
- [Calendar reference](references/calendar.md)
- [Drive reference](references/drive.md)
- [Sheets reference](references/sheets.md)
- [Tasks and Contacts reference](references/tasks-contacts.md)
- [REST API and deployment reference](references/rest-api.md)
- [MCP server reference](references/mcp.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI and Python examples; JSON when supported by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some CLI commands do not support JSON output.]

## Skill Version(s):

0.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
