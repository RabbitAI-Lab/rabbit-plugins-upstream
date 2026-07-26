## Description: <br>
Provides guidance for Google Workspace automation through gogcli-backed MCP servers for Docs, Sheets, Slides, Drive, and Classroom. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure gogcli MCP packages and route Google Workspace automation tasks to the appropriate Docs, Sheets, Slides, Drive, or Classroom toolset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent use a gogcli-authenticated Google account for broad Workspace automation, including document, file, classroom, and permission-changing actions. <br>
Mitigation: Install only the sub-packages needed, set GOG_ACCOUNT when multiple accounts exist, and review sensitive or permission-changing actions before allowing execution. <br>


## Reference(s): <br>
- [gogcli](https://github.com/chrischall/gogcli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP server configuration, package selection guidance, and gogcli authentication commands.] <br>

## Skill Version(s): <br>
2.17.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
