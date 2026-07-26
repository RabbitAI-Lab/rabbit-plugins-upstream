## Description: <br>
Coding Disciplines helps an agent enforce coding workflow gates, record recurring mistakes, and maintain project logs to reduce repeated coding errors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to apply strict coding discipline during software tasks, including pre-work file checks, step planning, verification, work-log updates, and mistake-pattern tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs broad automatic project documentation and log changes, which can modify repository state beyond the immediate coding task. <br>
Mitigation: Use it only in repositories where framework.md, WORK_LOG.md, MEMORY.md, and plan synchronization are expected, and review generated or modified files before committing. <br>
Risk: The skill includes an unsafe database deletion testing rule for project_data.db. <br>
Mitigation: Remove or override the database deletion rule before use, or require explicit confirmation before any destructive test setup runs. <br>
Risk: The skill can instruct command execution and file creation as part of its workflow gates. <br>
Mitigation: Require confirmation before command execution or new file creation in sensitive repositories and limit activation to trusted coding sessions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with workflow rules, checklists, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create or update project documentation, work logs, memory files, plan data, and validation commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
