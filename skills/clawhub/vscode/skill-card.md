## Description: <br>
Configures, debugs, and speeds up Visual Studio Code across settings scopes, launch.json, tasks.json, extensions, keybindings, formatters, remote work, workspace trust, and editor performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to diagnose and produce VS Code settings, launch configurations, tasks, extension recommendations, remote development guidance, and security checks for editor-centered workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically reads and writes persistent home-directory memory and shared host/project inventories under ~/Clawic/data. <br>
Mitigation: Install only when that long-lived local storage policy is acceptable, and review or modify the skill to require confirmation before writing or deleting those files. <br>
Risk: Editor configuration can contain credentials, host names, ports, paths, and other sensitive environment details. <br>
Mitigation: Do not use the skill in sensitive client or production environments unless the storage policy is approved, and store credential references only as pointers rather than secret values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/vscode) <br>
- [Clawic VSCode skill page](https://clawic.com/skills/vscode) <br>
- [Security guidance](security.md) <br>
- [Working file templates](memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON, YAML, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or update local VS Code memory files under ~/Clawic/data when durable editor decisions, configuration, or environment facts are produced.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
