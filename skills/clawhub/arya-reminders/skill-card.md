## Description: <br>
Creates one-time Spanish natural-language reminders for America/Bogota by emitting cron job JSON and logging reminders in Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[staratheris](https://clawhub.ai/user/staratheris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to turn Spanish reminder requests into one-shot scheduled reminders in America/Bogota, with local Markdown logging and cron delivery through OpenClaw. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reminder text may be delivered to the default hardcoded Telegram chat destination if the environment is not configured. <br>
Mitigation: Set ARYA_TELEGRAM_CHAT_ID to a verified chat ID before use and confirm the delivery destination before scheduling reminders. <br>
Risk: Reminder contents are stored locally and scheduled for future delivery, which may expose sensitive text through logs or external delivery paths. <br>
Mitigation: Avoid sensitive reminder text unless local storage and Telegram delivery are acceptable for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/staratheris/skills/arya-reminders) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Markdown, Guidance] <br>
**Output Format:** [JSON cron job request plus Markdown logging guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Timezone defaults to America/Bogota; Telegram delivery destination can be overridden with ARYA_TELEGRAM_CHAT_ID.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
