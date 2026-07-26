## Description: <br>
Send a quick email via SMTP using `msmtp` without opening a full mail client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to send simple SMTP email messages through msmtp, including messages with headers and optional cc, bcc, or attachments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send email and attachments through the user's SMTP account. <br>
Mitigation: Verify every recipient, message body, and attachment before sending. <br>
Risk: SMTP credentials may be exposed if they appear in prompts, logs, shell history, or committed files. <br>
Mitigation: Use a dedicated app password or scoped SMTP credential where possible, and keep SMTP_PASS out of prompts, logs, shell history, and files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/email-send) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires msmtp and SMTP_HOST, SMTP_PORT, SMTP_USER, and SMTP_PASS environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
