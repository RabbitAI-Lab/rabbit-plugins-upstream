## Description: <br>
Manage OmniFocus tasks, projects, folders, tags, due dates, recurring tasks, and task state through Omni Automation on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coyote-git](https://clawhub.ai/user/coyote-git) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users on macOS use this skill to let an agent query and update OmniFocus tasks, projects, folders, tags, dates, and recurring task settings. It is intended for local task management workflows where OmniFocus is installed and Automation access is deliberately granted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify local OmniFocus task data after macOS Automation access is granted. <br>
Mitigation: Grant Automation access only when you intend the agent to manage OmniFocus data, and review the agent's planned action before running commands that change tasks. <br>
Risk: Delete and other mutation commands can affect important tasks or projects. <br>
Mitigation: Ask the agent to show the target task details before destructive or important changes, especially delete, move, complete, due, defer, note, and repeat operations. <br>
Risk: Task notes may contain sensitive information that the agent could read or expose in conversation. <br>
Mitigation: Avoid storing secrets in OmniFocus task notes and review returned JSON before sharing it outside the local workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coyote-git/skills/omnifocus-automation) <br>
- [Publisher profile](https://clawhub.ai/user/coyote-git) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [JSON command responses with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate on local OmniFocus data and may read, create, modify, complete, move, or delete tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
