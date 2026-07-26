## Description: <br>
ClawConnect is a universal account connector for AI agents that can access Gmail, Calendar, Twitter, Slack, and Discord through one API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yiweil](https://clawhub.ai/user/yiweil) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to connect AI agents to user-authorized Gmail, Calendar, Twitter, Slack, and Discord accounts for account reads and actions such as sending messages, tweets, and email. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can concentrate broad read and send access for email, social, calendar, and workspace services behind one third-party API key. <br>
Mitigation: Connect only the services needed, verify scopes and revocation controls on clawconnect.dev, and keep the API key secret. <br>
Risk: Agent use of connected accounts can create account-changing actions such as tweets, emails, and Slack messages. <br>
Mitigation: Require explicit user confirmation before any tweet, email, Slack message, or other account-changing action. <br>


## Reference(s): <br>
- [ClawConnect service](https://clawconnect.dev) <br>
- [ClawHub skill page](https://clawhub.ai/yiweil/skills/clawconnect) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ClawConnect API key and connected user accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
