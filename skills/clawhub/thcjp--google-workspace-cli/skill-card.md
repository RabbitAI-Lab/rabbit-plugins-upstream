## Description: <br>
Guides an agent in using the gog command-line tool to automate Gmail, Calendar, Drive, Sheets, Docs, and Contacts workflows for Google Workspace accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, administrators, and developers use this skill to operate Google Workspace services through CLI-driven workflows such as sending mail, managing calendar events, exporting documents, and updating Sheets data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to send email or modify Google Workspace data through non-interactive gog CLI commands. <br>
Mitigation: Use least-privilege OAuth scopes, prefer test accounts for validation, and require explicit human review before sending mail, changing Sheets, deleting calendar data, or exporting sensitive documents. <br>
Risk: Commands may operate against live business data once Google OAuth credentials are configured. <br>
Mitigation: Confirm the active Google account and target resource IDs before execution, and keep --no-input disabled for risky tasks unless the workflow has been separately approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-workspace-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to execute gog CLI commands against live Google Workspace data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
