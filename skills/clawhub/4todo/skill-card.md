## Description: <br>
Manage 4todo from chat by capturing tasks, prioritizing them with the Eisenhower Matrix, reordering items, completing todos, and managing recurring tasks across workspaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blackstorm](https://clawhub.ai/user/blackstorm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and 4todo users use this skill to let an agent manage tasks and recurring todos in their 4todo workspaces while keeping API tokens out of chat and logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change a user's 4todo tasks using a user-provided API token. <br>
Mitigation: Install it only when task read/write access is intended, and provide the token through OpenClaw configuration, environment injection, or a secret store rather than chat. <br>
Risk: Broad reordering, completion, or recurring-task deletion actions can affect many tasks or workspaces. <br>
Mitigation: Review workspace and task names before performing large changes, and re-fetch tasks after mutations to verify the result. <br>


## Reference(s): <br>
- [4todo Skill Page](https://clawhub.ai/blackstorm/skills/4todo) <br>
- [4todo](https://4to.do) <br>
- [4todo API v0 Reference](references/api_v0.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with concise task summaries and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a user-provided FOURTODO_API_TOKEN and should avoid exposing internal IDs unless the user asks.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
