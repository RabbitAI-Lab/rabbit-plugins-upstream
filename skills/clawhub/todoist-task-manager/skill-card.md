## Description: <br>
Manage Todoist tasks via the `todoist` CLI, including listing, adding, modifying, completing, deleting, filtering, syncing, and viewing task details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2mawi2](https://clawhub.ai/user/2mawi2) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Todoist tasks through the installed `todoist` CLI. It supports routine task workflows such as listing, creating, updating, completing, deleting, syncing, and filtering tasks by project, label, priority, or due date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Todoist API token that grants account access. <br>
Mitigation: Install only if the agent should manage Todoist tasks, treat `~/.config/todoist/config.json` as secret, restrict file permissions, and avoid exposing the token in shell history or screenshots. <br>
Risk: Task modification, completion, and deletion commands can change or remove Todoist data. <br>
Mitigation: Verify task IDs and intended operations before running `complete`, `modify`, or `delete` commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/2mawi2/skills/todoist-task-manager) <br>
- [Todoist CLI Homepage](https://github.com/sachaos/todoist) <br>
- [Todoist Developer Token Settings](https://app.todoist.com/app/settings/integrations/developer) <br>
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters-V98wIH) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the `todoist` CLI and a Todoist API token configured in `~/.config/todoist/config.json`.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
