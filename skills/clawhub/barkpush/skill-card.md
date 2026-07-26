## Description: <br>
Bark Push helps agents send Bark notifications with multi-user targeting, content-type handling, history tracking, and message update support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liberalchang](https://clawhub.ai/user/liberalchang) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and automation agents use this skill to send Bark push notifications, manage recipient aliases and groups, and update or review notification history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification content, URLs, recipient device keys, and push parameters are sent to the configured Bark service. <br>
Mitigation: Install only when the Bark service is trusted and avoid putting secrets or sensitive content in notifications. <br>
Risk: Local configuration and history can include device keys, message text, and push metadata. <br>
Mitigation: Protect ~/.bark-push/config.json and ~/.bark-push/history.json and limit access to the state directory. <br>
Risk: Update and delete workflows retain history used to target previous pushes. <br>
Mitigation: Disable enable_update when update and delete history is not needed, and review broadcast, update, and delete commands before use. <br>


## Reference(s): <br>
- [Bark Website](https://bark.day.app) <br>
- [Bark API Documentation](https://bark.day.app/#/tutorial) <br>
- [ClawHub Skill Page](https://clawhub.ai/liberalchang/skills/barkpush) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can send notification content, URLs, recipient device keys, and push parameters to the configured Bark service.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
