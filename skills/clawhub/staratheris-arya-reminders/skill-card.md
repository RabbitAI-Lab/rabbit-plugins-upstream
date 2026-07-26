## Description: <br>
Creates one-shot reminders from Spanish natural-language time expressions using the America/Bogota timezone, emits cron job requests, and records reminder details in markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[staratheris](https://clawhub.ai/user/staratheris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to create scheduled reminders from Spanish conversational requests, especially when reminders should be interpreted in the America/Bogota timezone. The skill prepares a cron job request and supports markdown reminder logging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reminder text may be delivered to the default Telegram chat ID rather than the intended recipient. <br>
Mitigation: Set ARYA_TELEGRAM_CHAT_ID to a verified destination before creating reminders, or only install the skill when the default chat ID is intended. <br>
Risk: Sensitive reminder content may be stored in memory/reminders.md and delivered through Telegram. <br>
Mitigation: Avoid sensitive reminder text, review reminder logs, and confirm Telegram delivery is acceptable for the intended use. <br>
Risk: The documentation states that no external APIs or outside IDs are required, but security evidence reports Telegram delivery behavior. <br>
Mitigation: Review the delivery behavior before installation and treat Telegram configuration as required operational setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/staratheris/skills/staratheris-arya-reminders) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Agent usage note](artifact/create-reminder.agent.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [JSON cron job request with shell command usage and markdown logging guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and python3. Reminder delivery may use Telegram and reminder text may be stored in memory/reminders.md.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
