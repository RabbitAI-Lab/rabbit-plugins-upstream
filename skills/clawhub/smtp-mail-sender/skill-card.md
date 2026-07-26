## Description: <br>
通用 SMTP 邮件发送工具 helps an agent configure SMTP credentials and send plain text or HTML email with multiple recipients and attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antarctic-penguin971](https://clawhub.ai/user/antarctic-penguin971) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need an agent to send email reports, notifications, reminders, or messages with HTML bodies and attachments through a configured SMTP mailbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores reusable mailbox credentials persistently. <br>
Mitigation: Use an app-specific authorization code instead of an account password, avoid passing passwords on the command line, and remove the stored SMTP_MAIL_PWD value when the skill is no longer needed. <br>
Risk: The skill can send local files outward as email attachments. <br>
Mitigation: Confirm recipients, message content, and attachments before every send, and install only if agent access to the configured mailbox is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antarctic-penguin971/skills/smtp-mail-sender) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill invokes a Python SMTP sender that can configure credentials, check configuration, send HTML or plain text messages, and attach local files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
