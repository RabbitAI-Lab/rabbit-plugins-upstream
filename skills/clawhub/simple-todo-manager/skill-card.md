## Description: <br>
Manage simple todos with add, list, complete, and remove features using a configurable todo file, priority, and auto-archive settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoran-xc](https://clawhub.ai/user/zoran-xc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to let an agent maintain a simple workspace todo list in Markdown, including adding, listing, completing, removing, prioritizing, and auto-archiving tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill edits a configured local Markdown todo file and can remove or auto-archive completed tasks. <br>
Mitigation: Review the todo_file path before use, require confirmation before deletion, and set auto_archive_days to 0 when completed tasks should be kept indefinitely. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zoran-xc/skills/simple-todo-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown todo entries and concise chat responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Edits the configured workspace todo markdown file; no external services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
