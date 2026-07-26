## Description: <br>
Cron turns recurring intentions into structured local schedules for reminders, repeated tasks, and time-based execution plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and productivity-focused agent users use Cron to capture recurring jobs, inspect upcoming runs, and pause or resume local schedules. It supports local recurring-task planning without external sync or a third-party cron service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring schedules can repeat local actions if a job is configured incorrectly. <br>
Mitigation: Review each proposed schedule before activation, keep uncertain jobs paused, and inspect upcoming runs before relying on the schedule. <br>
Risk: Schedule and run history are stored locally under the skill platform workspace. <br>
Mitigation: Review or remove stored job and history files when the schedule data should no longer be retained. <br>


## Reference(s): <br>
- [Cron on ClawHub](https://clawhub.ai/thcjp/skills/cron) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with local file paths and command-oriented workflow names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local schedule records and run history when an agent implements the workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
