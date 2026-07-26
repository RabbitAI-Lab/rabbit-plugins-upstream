## Description: <br>
Create and manage scheduled reminders and recurring posts to Discord by turning natural-language timing requests into Moltbot cron jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronwander](https://clawhub.ai/user/aaronwander) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and Discord community operators use this skill to schedule one-time reminders or recurring posts that are delivered back to a captured Discord channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled or recurring jobs can post to Discord after the original chat has ended. <br>
Mitigation: Before enabling a job, verify the channel ID, timezone, schedule, message content, and how to list or cancel the job. <br>
Risk: Ambiguous Discord destinations can send scheduled messages to the wrong target. <br>
Mitigation: Use explicit channel:<id> or user:<id> targets, and ask for a Discord message link or channel ID when the current channel is not available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaronwander/skills/scheduler-for-discord) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create one-shot or recurring scheduled jobs that deliver messages to explicit channel IDs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
