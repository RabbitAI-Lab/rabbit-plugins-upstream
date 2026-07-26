## Description: <br>
AI README Manager helps agents discover, initialize, update, validate, and compress AI_README.md files so project conventions remain available across coding sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[draco-cheng](https://clawhub.ai/user/draco-cheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs project-specific coding conventions before editing, creating, or reviewing files, or when it needs to maintain AI_README.md convention files through the configured MCP tools. <br>

### Deployment Geography for Use: <br>
Global, wherever the user can run OpenClaw and the configured ai-readme-mcp server for repositories they are authorized to access. <br>

## Known Risks and Mitigations: <br>
Risk: The configured MCP context service can influence routine code work across repositories. <br>
Mitigation: Install only when the MCP service is trusted, scope use to repositories or files where shared conventions are needed, and review retrieved context before relying on it. <br>
Risk: Incorrect AI_README.md updates can preserve misleading project conventions for future agent sessions. <br>
Mitigation: Keep human review for AI_README changes and validate proposed conventions or architectural decisions before using them as persistent guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/draco-cheng/skills/ai-readme-manager) <br>
- [Publisher profile](https://clawhub.ai/user/draco-cheng) <br>
- [Package homepage from release metadata](https://github.com/Draco-Cheng/ai-readme-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language guidance, AI_README.md markdown content managed through MCP tools, shell command snippets, and JSON configuration examples.] <br>
**Output Parameters:** [Project root, target file path, existing AI_README.md content, repository conventions, and user-supplied architectural decisions.] <br>
**Other Properties Related to Output:** [Outputs are intended to guide agent behavior and should be reviewed before they affect persistent project conventions.] <br>

## Skill Version(s): <br>
1.7.2 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
