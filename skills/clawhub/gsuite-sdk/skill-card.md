## Description:

Work with Gmail, Google Calendar, Drive, Sheets, Tasks and Contacts, and read Search Console, Google Analytics 4 and Tag Manager, through the gsuite-sdk Python library and its `gsuite` CLI (JSON output for agents). Use it to read and send email, manage events, upload and share files, read and write spreadsheets, manage tasks and contacts, and pull search, traffic and tag data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to access Google Workspace services and read marketing analytics through the gsuite-sdk Python library or CLI. It supports common email, calendar, file, spreadsheet, task, contact, Search Console, Analytics, and Tag Manager workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Workspace access may expose private email, files, calendars, tasks, and contacts.

Mitigation: Grant only the Google permissions needed, protect saved login tokens, and confirm before sending email, inviting attendees, sharing files, or deleting data.

Risk: An exposed REST deployment could allow unauthorized access to connected Google services.

Mitigation: Keep REST deployments authenticated and restrict their exposure.

## Reference(s):

- [Google Suite documentation](https://pabloalaniz.github.io/google-suite/)
- [Google OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [Release notes for 0.13.0](https://github.com/PabloAlaniz/google-suite/releases/tag/v0.13.0)
- [Gmail reference](references/gmail.md)
- [Calendar reference](references/calendar.md)
- [Drive reference](references/drive.md)
- [Sheets reference](references/sheets.md)
- [Tasks and Contacts reference](references/tasks-contacts.md)
- [Search Console, Analytics and Tag Manager reference](references/marketing.md)
- [REST API and deployment reference](references/rest-api.md)
- [MCP server reference](references/mcp.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Code]

**Output Format:** [JSON CLI responses, Python SDK results, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google API access requires OAuth credentials and network access. Actions that send, share, invite, or delete should be confirmed first.]

## Skill Version(s):

0.13.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
