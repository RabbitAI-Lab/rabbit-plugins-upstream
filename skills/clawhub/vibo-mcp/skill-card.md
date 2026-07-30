## Description: <br>
Vibo MCP lets agents access and manage a user's Vibo event music planning, including events, timeline sections, song requests, playlists, and exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Vibo event hosts and planners use this skill to let an agent read event music details, manage timeline sections and song requests, and export event playlists through the Vibo MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP integration can access and modify Vibo event music data after authentication. <br>
Mitigation: Install only when the user trusts the vibo-mcp package and review each confirm:true write preview before approving a mutating action. <br>
Risk: Captured tokens or session files can grant access to the user's Vibo account. <br>
Mitigation: Protect VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, VIBO_EMAIL, VIBO_PASSWORD, and ~/.vibo-mcp/session.json like credentials, and avoid syncing them to shared backups. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp) <br>
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp) <br>
- [Vibo](https://vibodj.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [MCP write actions are confirm-gated and should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
