## Description: <br>
Google Tasks API integration with managed OAuth for managing task lists and tasks with full CRUD operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read, create, update, move, clear, and delete Google Tasks task lists and tasks through Maton's managed OAuth gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses configured service credentials to access Google Tasks through Maton. <br>
Mitigation: Use scoped API tokens where available, keep MATON_API_KEY out of shared repositories and skill memory, and install the skill only when that account access is intended. <br>
Risk: Create, update, move, clear, and delete operations can change or remove task data in the connected Google Tasks account. <br>
Mitigation: Require explicit user approval for write operations and confirm the target task list, task, and intended effect before execution. <br>
Risk: If multiple Google Tasks OAuth connections exist, requests may affect the wrong account or task list. <br>
Mitigation: Specify the intended connection ID when more than one connection is active and verify opaque task list and task IDs before write operations. <br>


## Reference(s): <br>
- [Google Tasks API Overview](https://developers.google.com/workspace/tasks) <br>
- [Google Tasks Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks) <br>
- [Google Tasks TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [ClawHub Google Tasks Skill](https://clawhub.ai/byungkyu/skills/google-tasks-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations should be explicitly approved before execution.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
