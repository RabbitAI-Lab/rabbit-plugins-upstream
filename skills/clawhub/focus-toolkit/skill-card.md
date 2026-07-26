## Description: <br>
Full focus lifecycle: natural-language alarms, pomodoro tracking, ambient soundscapes, and attention analytics in one skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eelowl](https://clawhub.ai/user/eelowl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to manage focus sessions through reminders, pomodoro state tracking, generated background sound, and daily or weekly attention reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create reminders or recurring reminder schedules that may persist after the chat session. <br>
Mitigation: Be explicit about reminder times and recurrence, and remove unwanted recurring reminders through the environment's normal reminder or cron controls. <br>
Risk: The skill keeps local pomodoro history and can generate local focus reports. <br>
Mitigation: Install it only when local focus tracking is desired, and review local history files according to your environment's data-retention practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eelowl/skills/focus-toolkit) <br>
- [Packaged skill overview](artifact/skill.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON status output, local report text, reminder configuration, and generated WAV files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create local reminder schedules, pomodoro history, focus reports, and ambient sound files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
