## Description: <br>
TickTick Tasks helps agents manage TickTick projects and tasks, including listing projects and tasks, creating tasks, completing tasks, and deleting tasks after OAuth setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaiofreitas](https://clawhub.ai/user/kaiofreitas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage TickTick task lists through an agent, including project review, task creation, completion, deletion, and reminder-oriented task entry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth setup requires providing a TickTick client secret to a local setup command. <br>
Mitigation: Verify the ticktick-setup executable and install source before entering credentials. <br>
Risk: Complete and delete actions can change or remove TickTick tasks. <br>
Mitigation: Review project and task IDs before approving completion or deletion commands. <br>
Risk: The skill depends on external ticktick command-line tools. <br>
Mitigation: Install only trusted executables and confirm which command path will run before use. <br>


## Reference(s): <br>
- [TickTick Developer Portal](https://developer.ticktick.com) <br>
- [TickTick Open API Base URL](https://api.ticktick.com/open/v1) <br>
- [ClawHub Skill Page](https://clawhub.ai/kaiofreitas/skills/ticktick-tasks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and concise task-management guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TickTick OAuth setup instructions and task or project command examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
