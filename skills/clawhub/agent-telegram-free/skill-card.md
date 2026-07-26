## Description: <br>
Agent Telegram Free defines a lightweight Telegram notification convention for main, backend, and frontend agents, including account IDs, emoji prefixes, fixed recipient routing, and start/completion message templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to standardize basic Telegram progress notifications from supported agent roles to the configured Telegram recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task details may be sent to the fixed Telegram ID 5440561025. <br>
Mitigation: Use the skill only when that recipient is intended, and avoid sending secrets, sensitive task details, absolute paths, or customer/project data. <br>
Risk: The skill declares shell execution even though its main behavior is message formatting and Telegram notification guidance. <br>
Mitigation: Review before installation and remove or restrict exec access unless the deployment specifically needs it. <br>
Risk: Telegram delivery depends on a configured message tool and protected Telegram bot token. <br>
Mitigation: Store bot tokens only in the platform configuration or secret manager and verify account routing before sending production updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-telegram-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [ClawDis homepage](https://skillhub.cn) <br>
- [Telegram Bot API](https://api.telegram.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Code] <br>
**Output Format:** [Markdown instructions with JSON-like message examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Messages target Telegram ID 5440561025 and require a configured message tool and Telegram bot token.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
