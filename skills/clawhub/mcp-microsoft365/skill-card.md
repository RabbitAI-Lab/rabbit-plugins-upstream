## Description: <br>
Integrates Microsoft 365 with agents through an MCP server for Outlook email, calendar events, OneDrive files, Microsoft To Do tasks, Teams chats, and user profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[makhatib](https://clawhub.ai/user/makhatib) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Microsoft 365 administrators use this skill to let an agent inspect and act on Microsoft 365 resources through Microsoft Graph. It supports mailbox, calendar, file, task, Teams, and user-profile workflows after Azure Entra ID credentials and Graph permissions are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad tenant-wide Microsoft Graph permissions and can read sensitive mail, files, chats, tasks, calendars, and user data. <br>
Mitigation: Install only for authorized Microsoft 365 administrators, prefer least-privilege or separate read-only and write deployments, and store Azure credentials securely. <br>
Risk: The skill exposes write actions such as sending mail or Teams messages and creating calendar events or tasks without built-in confirmation controls. <br>
Mitigation: Add explicit approval controls and audit logging before enabling send, create, or file-content read workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/makhatib/skills/mcp-microsoft365) <br>
- [Azure Portal](https://portal.azure.com) <br>
- [Author website](https://malkhatib.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and MCP tool responses, including JSON-formatted Microsoft Graph results and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes Microsoft 365 tenant data through Microsoft Graph; file reads are truncated to 50000 characters.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
