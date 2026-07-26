## Description: <br>
Coordinate work across human and AI agents using the Tick protocol and Git-backed TICK.md task files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gianni-dalerta](https://clawhub.ai/user/gianni-dalerta) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to let agents create, claim, update, validate, and complete project tasks in a shared Markdown task file. It supports local CLI workflows and optional MCP tooling for multi-agent coordination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete project task records in TICK.md as part of normal task coordination. <br>
Mitigation: Review proposed task changes, use dry-run or status commands before destructive operations, and require explicit approval for deletes, force deletes, direct edits, and non-dry-run undo. <br>
Risk: MCP configuration changes can alter an editor or agent environment. <br>
Mitigation: Back up config files and apply MCP config changes only with explicit user approval. <br>
Risk: Git push or tick sync push commands can send project task data to a remote repository. <br>
Mitigation: Use pull-only sync by default and run push commands only after explicit user approval. <br>
Risk: Task comments and history may expose sensitive information if users or agents include secrets. <br>
Mitigation: Avoid putting secrets, credentials, or private data in task comments or TICK.md history. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gianni-dalerta/skills/tick-md) <br>
- [Installation Guide](INSTALL.md) <br>
- [MCP Tools Reference](mcp-reference.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [tick-md npm Package](https://npmjs.com/package/tick-md) <br>
- [tick-mcp-server npm Package](https://npmjs.com/package/tick-mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and MCP tool examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to guide an agent's task coordination actions and may result in local TICK.md updates when approved workflows are followed.] <br>

## Skill Version(s): <br>
1.3.3 (source: skill.json, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
