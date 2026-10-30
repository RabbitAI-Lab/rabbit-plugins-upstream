## Description:

Work with Gmail, Google Calendar, Drive, Sheets, Tasks and Contacts, and read Search Console, Google Analytics 4 and Tag Manager, through the gsuite-sdk Python library and its `gsuite` CLI (JSON output for agents). Use it to read and send email, manage events, upload and share files, read and write spreadsheets, manage tasks and contacts, and pull search, traffic and tag data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use an authorized Google Workspace account to retrieve and update email, calendars, files, spreadsheets, tasks, and contacts, and to read Search Console, Analytics, and Tag Manager data. They can work through the gsuite CLI, Python SDK, MCP server, or REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Workspace access can expose or change sensitive account data.

Mitigation: Grant only the scopes needed, protect OAuth credential and token files, and confirm before sending email, inviting attendees, sharing files, or deleting data.

Risk: A deployed REST API can expose account operations if access is not restricted.

Mitigation: Protect the service with its API key and restrict access to the deployment.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [Google OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [ClawHub skill page](https://clawhub.ai/pabloalaniz/skills/gsuite-sdk)
- [Release notes (user-provided)](https://github.com/PabloAlaniz/google-suite/releases/tag/v0.9.0)

## Skill Output:

**Output Type(s):** [JSON, Text, Files, Code, Shell commands, Guidance]

**Output Format:** [JSON or text results, with optional downloaded or exported files; usage guidance includes Python snippets and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [File exports may include PDF, XLSX, CSV, and other Google Workspace formats; available operations depend on configured OAuth scopes.]

## Skill Version(s):

0.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
