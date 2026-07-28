## Description: <br>
Provides Google Workspace automation through gogcli MCP servers for Docs, Sheets, Slides, Drive, and Classroom. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to configure and use gogcli-backed MCP servers for Google Workspace document, spreadsheet, presentation, file, and classroom automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a gogcli-authenticated Google account to affect real Docs, Sheets, Drive, Slides, and Classroom data. <br>
Mitigation: Install it only when Google Workspace automation is intended and review write, sharing, deletion, grading, and permission-changing actions before allowing them. <br>
Risk: Automation may run against the wrong Google account when multiple accounts are authenticated. <br>
Mitigation: Set GOG_ACCOUNT in the MCP environment to the intended account before use. <br>
Risk: Installing unnecessary sub-packages can expose broader Google Workspace automation surfaces than the task requires. <br>
Mitigation: Prefer installing only the gogcli MCP sub-packages needed for the intended Docs, Sheets, Slides, Drive, or Classroom workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp) <br>
- [gogcli project](https://github.com/chrischall/gogcli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct users to sibling MCP packages for specific Google Workspace APIs.] <br>

## Skill Version(s): <br>
2.18.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
