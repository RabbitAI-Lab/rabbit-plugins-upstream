## Description: <br>
Access and manage Microsoft 365 email, calendar, OneDrive files, To Do tasks, and contacts through Microsoft Graph with authentication support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cvsloane](https://clawhub.ai/user/cvsloane) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to let an agent inspect and manage Microsoft 365 services such as Outlook mail, calendars, OneDrive files, To Do tasks, and contacts. It is useful for account-aware productivity workflows that need Microsoft Graph access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify sensitive Microsoft 365 account data through delegated Microsoft Graph permissions. <br>
Mitigation: Grant the narrowest practical Graph permissions, prefer read-only mode where possible, and require explicit confirmation before sending mail, changing calendars, uploading or deleting files, modifying tasks, or posting to Teams. <br>
Risk: The skill executes an external npm MCP server package during Microsoft 365 operations. <br>
Mitigation: Install only if the Softeria MCP package is trusted, pin or otherwise control the npm dependency, and review dependency updates before deployment. <br>
Risk: Client secrets and tenant credentials may be needed for headless operation. <br>
Mitigation: Store secrets in a secret manager or equivalent protected configuration and avoid exposing them in logs, prompts, or shared configuration files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cvsloane/skills/ms365) <br>
- [@softeria/ms-365-mcp-server package](https://www.npmjs.com/package/@softeria/ms-365-mcp-server) <br>
- [Softeria ms-365-mcp-server repository](https://github.com/Softeria/ms-365-mcp-server) <br>
- [Azure Portal](https://portal.azure.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and command output from Microsoft 365 operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Microsoft 365 account data, message content, calendar data, file metadata, task data, contact records, and operation status responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
