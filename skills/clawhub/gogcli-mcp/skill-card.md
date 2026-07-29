## Description: <br>
Provides an umbrella skill for Google Workspace automation via gogcli across Docs, Sheets, Slides, Drive, and Classroom, with sibling packages for specific APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Workspace operators use this skill to configure and direct gogcli-backed MCP servers for Google Docs, Sheets, Slides, Drive, and Classroom tasks. It is intended for authenticated automation against the locally configured Google account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on live Google Workspace data through the locally configured gogcli account, including business, school, or shared Drive data. <br>
Mitigation: Review the account and data scope before installing or running it, especially in business, school, or shared-drive environments. <br>
Risk: On machines with multiple Google accounts, automation may target the wrong account if the account is not selected explicitly. <br>
Mitigation: Set GOG_ACCOUNT explicitly in MCP environment configuration. <br>
Risk: Edits, permission changes, uploads, downloads, and Classroom grading actions can modify user or organization data. <br>
Mitigation: Require clear user confirmation before carrying out write, permission, transfer, or grading actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp) <br>
- [gogcli project](https://github.com/chrischall/gogcli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP server configuration and account-selection guidance for gogcli-backed Google Workspace automation.] <br>

## Skill Version(s): <br>
2.18.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
