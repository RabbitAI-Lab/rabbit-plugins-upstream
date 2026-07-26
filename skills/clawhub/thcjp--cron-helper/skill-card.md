## Description: <br>
Schedule and manage recurring tasks for your agent, including cron jobs, timers, execution history, and timezone-aware automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to create, list, pause, resume, delete, and inspect recurring agent tasks without manually writing cron syntax. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring agent tasks can repeatedly trigger actions that access accounts, execute commands, or consume resources. <br>
Mitigation: Review each scheduled task before adding it, avoid broad tasks involving sensitive accounts or open-ended commands, and periodically audit active tasks with list, log, and delete controls. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/cron-helper) <br>
- [ClawSwarm related project](https://onlyflies.buzz/clawswarm/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose recurring task definitions that require user review before scheduling.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
