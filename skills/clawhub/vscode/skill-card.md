## Description: <br>
Configures and troubleshoots Visual Studio Code settings, debugging, tasks, extensions, keybindings, formatting, remote development, performance, and workspace security. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to diagnose and update VS Code configuration, debugging, task, extension, remote-development, and workspace-security setup. It is especially suited for editor behavior that depends on settings scope, extension placement, workspace trust, or persisted local notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically reads, writes, and restructures persistent local notes and shared host or project inventories. <br>
Mitigation: Install only when that persistence model is acceptable, review the files under the declared config paths periodically, and avoid using it for highly sensitive projects. <br>
Risk: VS Code workspace configuration can enable task execution, extension behavior, and executable-path settings once a folder is trusted. <br>
Mitigation: Review repository .vscode files, devcontainer lifecycle commands, and extension recommendations before trusting an unreviewed folder or applying generated configuration. <br>
Risk: Editor settings, task definitions, launch configurations, and terminal environment blocks can contain credentials. <br>
Mitigation: Store credential pointers rather than secret values, and keep tokens, keys, passwords, and private keys out of local memory notes and committed workspace configuration. <br>


## Reference(s): <br>
- [ClawHub VSCode Skill Page](https://clawhub.ai/ivangdavila/skills/vscode) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic VSCode Skill](https://clawic.com/skills/vscode) <br>
- [Clawic](https://clawic.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands.] <br>
**Output Parameters:** [Single response stream.] <br>
**Other Properties Related to Output:** [May propose changes to VS Code settings, launch, tasks, keybindings, extensions, workspace files, and local memory notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
