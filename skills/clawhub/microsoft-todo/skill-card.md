## Description: <br>
Manage Microsoft To Do tasks via the `todo` CLI, including adding, listing, completing, removing, and organizing tasks, subtasks, notes, and lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[underwear](https://clawhub.ai/user/underwear) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to manage Microsoft To Do tasks, lists, notes, and steps through the `todo` CLI after configuring Microsoft Azure OAuth credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deletion commands can remove Microsoft To Do tasks, steps, notes, or lists, and the artifact recommends bypassing CLI confirmation prompts. <br>
Mitigation: Require explicit user confirmation before destructive operations, show the exact target, and prefer stable task IDs over indexes or names. <br>
Risk: The skill requires local Microsoft OAuth credentials and token files for Microsoft To Do access. <br>
Mitigation: Treat `keys.yml` and OAuth token files as secrets, restrict local file permissions, avoid logging or pasting their contents, and rotate the Azure client secret if exposed. <br>
Risk: The upstream `microsoft-todo-cli` package receives access to the user's Microsoft To Do data. <br>
Mitigation: Install and use the package only when the upstream package and requested Microsoft permissions are trusted. <br>


## Reference(s): <br>
- [Microsoft To Do skill page](https://clawhub.ai/underwear/skills/microsoft-todo) <br>
- [Microsoft To Do CLI homepage](https://github.com/underwear/microsoft-todo-cli) <br>
- [Setting Up Microsoft API Access](references/setup.md) <br>
- [Azure Portal](https://portal.azure.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands commonly request JSON output from the `todo` CLI for structured task data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
