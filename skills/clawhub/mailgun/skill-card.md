## Description: <br>
Send emails via Mailgun API for newsletters, notifications, alerts, and automated reports when Mailgun credentials are configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to send transactional or automated emails through their Mailgun account from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Emails are sent through a third-party Mailgun account using user-provided credentials. <br>
Mitigation: Use a narrowly scoped Mailgun key where possible and protect credentials stored in shell or config files. <br>
Risk: Message content or recipients could include sensitive or regulated data. <br>
Mitigation: Review recipients and message content before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manifoldor/skills/mailgun) <br>
- [Project homepage](https://github.com/openclaw/openclaw) <br>
- [Mailgun documentation](https://documentation.mailgun.com/) <br>
- [Mailgun API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Text] <br>
**Output Format:** [Command-line execution with plain-text status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Mailgun account credentials and configured sender and recipient values.] <br>

## Skill Version(s): <br>
1.0.6 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
