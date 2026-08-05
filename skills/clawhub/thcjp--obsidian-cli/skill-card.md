## Description: <br>
Helps an agent operate Obsidian through CLI-oriented guidance for vault file operations, templates, plugins, themes, sync, history, developer tools, workspaces, and TUI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and advanced Obsidian users use this skill to ask an agent for command-oriented help managing Obsidian vaults, automation, plugins, sync, file history, and debugging workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward broad changes in an Obsidian vault, including delete, overwrite, move, plugin, sync restore/delete, eval, and watch-command actions. <br>
Mitigation: Use it only with a specific vault, keep backups, and require explicit approval before destructive, sync, plugin, eval, or watch-command operations. <br>
Risk: The security review states that the skill grants broad file, plugin, sync, JavaScript eval, and watch-command authority without enough guardrails. <br>
Mitigation: Review before installing, constrain the agent environment, and avoid using it around notes or configuration files that contain secrets unless containment is clear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/obsidian-cli) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command examples, configuration steps, troubleshooting notes, and operational cautions for Obsidian CLI workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
