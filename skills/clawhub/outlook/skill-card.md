## Description: <br>
Read, search, and manage Outlook emails and calendar via Microsoft Graph API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jotamed](https://clawhub.ai/user/jotamed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and users with Microsoft Outlook accounts use this skill to inspect mailbox state, search and read messages, send or reply to mail, and manage calendar events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify Outlook mail, send email as the user, and edit calendar events. <br>
Mitigation: Review every send, delete, bulk mail, and calendar-changing action before execution. <br>
Risk: OAuth client secrets and access or refresh tokens are stored locally and can be exposed if printed or shared. <br>
Mitigation: Treat ~/.outlook-mcp as sensitive credential storage, keep file permissions restricted, avoid printing access tokens, and rotate credentials if exposure is suspected. <br>
Risk: The security guidance flags unsafe local file and credential-handling behavior, including attachment path handling. <br>
Mitigation: Avoid downloading attachments to sensitive paths until path handling is fixed and review generated file paths before use. <br>


## Reference(s): <br>
- [ClawHub Outlook Skill Page](https://clawhub.ai/jotamed/skills/outlook) <br>
- [Outlook Manual Setup Guide](references/setup.md) <br>
- [Azure Portal](https://portal.azure.com) <br>
- [Microsoft Graph API Endpoint](https://graph.microsoft.com/v1.0/me) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown instructions with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Azure CLI and jq for setup; stores OAuth configuration and credentials under ~/.outlook-mcp.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
