## Description: <br>
Use when managing todos, tasks, projects, or kanban boards via Taskleef.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xatter](https://clawhub.ai/user/xatter) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Taskleef todos, projects, subtasks, and kanban boards through the Taskleef CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live changes to a Taskleef account, including completing or deleting todos, deleting projects, clearing board columns, and moving cards. <br>
Mitigation: Require explicit user confirmation before destructive or bulk-changing commands, especially delete, project delete, board clear, and partial-match operations. <br>
Risk: The skill depends on TASKLEEF_API_KEY for account access. <br>
Mitigation: Keep the API key out of shared files and logs, and provide it only through the configured environment or approved agent secret handling. <br>
Risk: The installer metadata downloads the Taskleef todo CLI from a remote URL. <br>
Mitigation: Review or pin the downloaded CLI before use in controlled environments. <br>


## Reference(s): <br>
- [Taskleef website](https://taskleef.com) <br>
- [ClawHub skill page](https://clawhub.ai/xatter/skills/taskleef) <br>
- [Taskleef CLI installer](https://raw.githubusercontent.com/Xatter/taskleef/main/taskleef-cli/todo) <br>
- [jq Linux x86_64 release](https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64) <br>
- [jq Linux ARM64 release](https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-arm64) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with inline shell commands and Taskleef CLI arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke live Taskleef account operations through the todo CLI when the agent is authorized.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
