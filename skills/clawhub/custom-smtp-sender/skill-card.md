## Description: <br>
Sends SMTP email using an existing local SMTP configuration, with support for HTML-formatted message bodies and file attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scccmsd](https://clawhub.ai/user/scccmsd) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to send SMTP email messages with a configured sender account, including HTML bodies and optional local file attachments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use stored SMTP credentials to send email through the configured account. <br>
Mitigation: Use a dedicated low-privilege SMTP account or app password and keep the SMTP configuration file restricted. <br>
Risk: The skill can send arbitrary local files as attachments without built-in confirmation or path limits. <br>
Mitigation: Check the exact recipient, subject, body source, and attachment paths before invoking the skill. <br>
Risk: Advertised retry, logging, and markdown conversion behavior is not reliable in the provided implementation. <br>
Mitigation: Do not rely on those features unless the implementation is updated and reviewed again. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scccmsd/skills/custom-smtp-sender) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/scccmsd) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [CLI-style email parameters and SMTP email content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local SMTP configuration file and can include attachments from specified local paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
