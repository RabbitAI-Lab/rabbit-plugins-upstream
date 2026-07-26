## Description: <br>
TickTick task manager integration for listing projects and tasks, creating tasks, completing tasks, and deleting tasks after OAuth setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaiofreitas](https://clawhub.ai/user/kaiofreitas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to manage TickTick to-do items from an agent session, including listing projects, reviewing tasks, adding reminders, and marking or deleting tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on external ticktick and ticktick-setup commands that access a user's TickTick account. <br>
Mitigation: Install only a trusted implementation of those commands and keep OAuth client secrets private. <br>
Risk: Complete and delete commands can change or remove TickTick tasks. <br>
Mitigation: Confirm the project and task identifiers before running completion or deletion commands. <br>


## Reference(s): <br>
- [ClawHub TickTick API skill page](https://clawhub.ai/kaiofreitas/skills/ticktick-api) <br>
- [TickTick Developer site](https://developer.ticktick.com) <br>
- [TickTick Open API base URL](https://api.ticktick.com/open/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and concise task-management guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses external ticktick and ticktick-setup commands; users should verify targets before complete or delete operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
