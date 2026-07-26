## Description: <br>
Gmail, Calendar, Drive, Docs, Sheets, and other Google Workspace tools through OAuth sign-in without Google Cloud Console setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dru-ca](https://clawhub.ai/user/dru-ca) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to configure and call a Google Workspace MCP server through mcporter for Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, People, and time workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and runs an unpinned third-party MCP server with persistent OAuth access to Google Workspace data. <br>
Mitigation: Review the package before installation, verify OAuth consent scopes during sign-in, and revoke the Google app access when the skill is no longer needed. <br>
Risk: Available tools can read, send, modify, or delete mail, calendar events, files, documents, and chat messages. <br>
Mitigation: Require explicit confirmation before sending messages, modifying files or mail, changing calendar data, or deleting anything. <br>
Risk: Local OAuth credentials persist under ~/.config/google-workspace-mcp/. <br>
Mitigation: Protect the local credential directory, clear it during decommissioning, and re-authenticate only with an account appropriate for the intended Workspace access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dru-ca/skills/google-workspace-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter and Google OAuth sign-in; credentials are stored under ~/.config/google-workspace-mcp/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
