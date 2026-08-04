## Description: <br>
Google Workspace CLI is an official Google release for managing Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and other Workspace APIs via CLI or native MCP server mode for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to install and operate the Google Workspace CLI for managing Workspace services or exposing selected Workspace APIs through MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated CLI or MCP use can operate on real Google Workspace mail, files, calendars, chat, and admin data. <br>
Mitigation: Use the narrowest OAuth scopes and MCP service list practical, prefer test accounts for automation, and start with dry-run or read-only commands before allowing sends, shares, calendar writes, or admin actions. <br>
Risk: OAuth credentials and account setup are required before first use. <br>
Mitigation: Complete the one-time authentication setup deliberately and protect credential files and service-account material according to the workspace owner's policy. <br>


## Reference(s): <br>
- [Google Workspace CLI repository](https://github.com/googleworkspace/cli) <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/skill-gws) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides CLI installation, authentication, usage, and MCP server configuration guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
