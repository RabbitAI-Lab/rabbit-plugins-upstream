## Description: <br>
为大型语言模型和AI代理提供外部工作记忆和任务管理功能，支持复杂多步骤任务的可靠执行。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to maintain an external task list for multi-step work, read current todos, and write structured task updates through the XiaoBenYang API. It requires an API key before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill presents as task management while including unrelated API-key and school-search behavior. <br>
Mitigation: Review the installed behavior before use and install only when the task-management and API-key requirements are intended. <br>
Risk: The artifact stores XBY_APIKEY in a local .env file and also reads it from the environment. <br>
Mitigation: Confirm where the key is stored, restrict workspace access, and rotate or remove the key when no longer needed. <br>
Risk: Dependencies are specified with minimum versions rather than exact reviewed versions. <br>
Mitigation: Pin and review dependency versions before deploying in a controlled or production environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/xby-todolist) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text summarizing JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; tool calls return success, raw, and message fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
