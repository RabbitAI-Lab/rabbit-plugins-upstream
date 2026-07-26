## Description: <br>
Creates OpenClaw cron jobs from natural language reminders or messages, supporting one-shot and recurring schedules with run-guard rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gostlightai](https://clawhub.ai/user/gostlightai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use Casual Cron to turn reminder requests or /at and /every commands into OpenClaw cron jobs for Telegram, WhatsApp, Slack, Discord, or Signal delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A scheduled job could send a message to the wrong recipient or external channel. <br>
Mitigation: Before approving job creation, verify the channel, destination, and exact message text with the user. <br>
Risk: Timezone or recurrence parsing could schedule the job at the wrong time or create an unintended recurring reminder. <br>
Mitigation: Confirm the timezone, parsed run time, recurrence, and one-shot deletion behavior before execution. <br>
Risk: Recurring jobs can continue delivering messages until changed or removed. <br>
Mitigation: Make recurring behavior explicit during confirmation and prefer one-shot jobs with delete-after-run for single reminders. <br>


## Reference(s): <br>
- [Casual Cron on ClawHub](https://clawhub.ai/gostlightai/skills/casual-cron) <br>
- [gostlightai publisher profile](https://clawhub.ai/user/gostlightai) <br>
- [Artifact skill documentation](artifact/SKILL.md) <br>
- [Artifact changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with inline OpenClaw shell commands; helper output may be JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cron job details for user confirmation before execution.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
