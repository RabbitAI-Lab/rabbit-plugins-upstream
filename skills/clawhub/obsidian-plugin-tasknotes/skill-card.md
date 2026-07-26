## Description: <br>
Manage Obsidian tasks through the TaskNotes plugin API, including listing, creating, updating, deleting, and filtering tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benoitjadinon](https://clawhub.ai/user/benoitjadinon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Obsidian users use this skill to manage TaskNotes tasks from an agent workflow, including task creation, task review, status updates, project filtering, and task deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete tasks or make broad task updates through the TaskNotes API. <br>
Mitigation: Ask for explicit user confirmation before deletes or broad updates. <br>
Risk: A TaskNotes API token may be exposed if the vault .env file is shared or committed. <br>
Mitigation: Keep the .env file private and store TASKNOTES_API_KEY only in the local vault environment. <br>
Risk: Exposing the TaskNotes HTTP API beyond the local machine could allow unintended access to task data. <br>
Mitigation: Keep the TaskNotes API bound to localhost and use an API token. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/benoitjadinon/skills/obsidian-plugin-tasknotes) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or table-formatted CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate against a local TaskNotes HTTP API and may read or modify tasks in the user's Obsidian vault.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
