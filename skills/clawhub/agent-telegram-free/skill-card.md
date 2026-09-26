## Description: <br>
agent-telegram-free defines Telegram notification conventions for agents, including role-to-account mappings, message formats, and start/completion reporting templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to standardize Telegram progress notifications from main, backend, and frontend agents. It is intended for basic task-start and task-completion reporting to a configured Telegram recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task details and file paths may be sent to fixed Telegram ID 5440561025. <br>
Mitigation: Install only when that Telegram ID is the intended recipient; change the destination and token handling before using it elsewhere. <br>
Risk: The skill asks for broader agent powers than its Telegram notification purpose requires. <br>
Mitigation: Restrict permissions to the minimum needed for message formatting and delivery, and review the skill before installation. <br>
Risk: Telegram notifications can expose sensitive workspace information outside the agent environment. <br>
Mitigation: Avoid sensitive workspaces unless the destination, content policy, and credential handling have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-telegram-free) <br>
- [Telegram Bot API](https://api.telegram.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and JavaScript-style message examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Messages are routed through a Telegram message tool and may include task details, completion summaries, and file paths.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
