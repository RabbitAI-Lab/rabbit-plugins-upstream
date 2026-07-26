## Description: <br>
Send emails via SMTP with runtime-injected account credentials and optional attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fontstep](https://clawhub.ai/user/fontstep) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to send plain-text email messages and optional file attachments through a configured SMTP account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send email content and chosen attachments outside the local environment. <br>
Mitigation: Install only when agent-driven email sending is intended, and verify recipients, subject, body, and attachment paths before sending. <br>
Risk: The included shell helper can use msmtp or mutt behavior if invoked. <br>
Mitigation: Prefer the Python SMTP workflow unless msmtp or mutt behavior is explicitly desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fontstep/skills/send-email) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can send message content and selected attachments through the configured SMTP account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
