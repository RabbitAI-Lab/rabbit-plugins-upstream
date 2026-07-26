## Description: <br>
Manage todos via Tasktrove API. Use for listing, creating, completing, or updating tasks. Triggers on task/todo requests like "what's on my todo list", "add a task", "mark X done", "what's due today". <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[willwebberley](https://clawhub.ai/user/willwebberley) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a configured Tasktrove instance for listing, creating, completing, updating, and searching todo tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can connect an agent to a Tasktrove server and modify task state. <br>
Mitigation: Use only a trusted TASKTROVE_HOST and require clear confirmation before completing, updating, or deleting tasks. <br>
Risk: An optional TASKTROVE_TOKEN may grant access to a user's Tasktrove data. <br>
Mitigation: Protect TASKTROVE_TOKEN as a secret and prefer HTTPS or a trusted local network. <br>


## Reference(s): <br>
- [Tasktrove](https://tasktrove.io) <br>
- [Tasktrove GitHub Repository](https://github.com/dohsimpson/tasktrove) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a configured Tasktrove API using TASKTROVE_HOST and optional TASKTROVE_TOKEN.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
