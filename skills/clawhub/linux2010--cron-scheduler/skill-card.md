## Description: <br>
Create, list, edit, and remove cron jobs to automate system tasks on a schedule, handling cron syntax and output management for you. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linux2010](https://clawhub.ai/user/linux2010) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect existing cron entries and prepare commands for scheduling, updating, testing, and removing recurring system tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent scheduled jobs may be installed without enough confirmation. <br>
Mitigation: Review each cron line, require an exact preview or dry run, and approve the final crontab change before installation. <br>
Risk: Crontab edits or broad removal patterns can remove or change existing scheduled work. <br>
Mitigation: Back up the current crontab before changes and avoid broad delete patterns such as removing lines by vague text matches. <br>
Risk: Scheduled jobs can become difficult to audit or clean up. <br>
Mitigation: Require every job to have a clear owner, log path, and removal plan before it is added. <br>


## Reference(s): <br>
- [Cron Scheduler on ClawHub](https://clawhub.ai/linux2010/skills/cron-scheduler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and cron expressions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposed crontab entries and shell commands that should be reviewed before installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
