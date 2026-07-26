## Description: <br>
定时调度专家 helps agents define and maintain local recurring or one-time scheduled jobs with timezone locking, previews, retries, cleanup, and audit history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn recurring checks, reminders, reports, data syncs, and health probes into auditable local schedules. It is suited for agents that need predictable task timing without relying on cloud scheduling services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled jobs can repeatedly run tasks that read private files, call APIs, sync data, or write reports beyond the user's intent. <br>
Mitigation: Review each task before creating a job, especially tasks with file, API, sync, or reporting behavior. <br>
Risk: Persistent local job records can accumulate active or outdated automations if they are not reviewed. <br>
Mitigation: Use the skill's documented list, pause, archive, stats, and cleanup workflows to audit active and archived jobs regularly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-scheduler-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local scheduling guidance, command patterns, job configuration examples, and audit workflows for agent-maintained cron-style tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
