## Description: <br>
Natural-language reminder secretary: capture events into git-synced workspace, schedule Telegram reminders via OpenClaw cron, and answer upcoming schedule queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[reed1898](https://clawhub.ai/user/reed1898) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to capture meetings, birthdays, deadlines, and other reminders from natural-language chat, then save structured events and schedule Telegram notifications. It also supports upcoming-event queries against the saved reminder file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reminder text and schedule details are saved locally in a workspace file that may be synced or shared. <br>
Mitigation: Avoid storing sensitive reminders in shared or synced workspaces, and review workspace sync settings before relying on the skill. <br>
Risk: Natural-language dates, relative times, lunar birthdays, or missing times can be resolved incorrectly. <br>
Mitigation: Use explicit wording when creating reminders and review the resolved datetime before relying on scheduled notifications. <br>
Risk: The default timezone is Asia/Shanghai, which may not match the user's location. <br>
Mitigation: Set REMINDER_TZ to the intended timezone before scheduling reminders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/reed1898/skills/reminder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with resolved reminder details and scheduling confirmations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes reminder data to ~/.openclaw/workspace/reminders/events.yml and schedules Telegram notifications through OpenClaw cron.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
