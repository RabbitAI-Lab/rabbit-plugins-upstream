## Description: <br>
Email API for AI agents to send and receive emails programmatically via ClawMail. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heyarviind](https://clawhub.ai/user/heyarviind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to configure a dedicated ClawMail inbox, poll for incoming email, send messages, and inspect email threads through the ClawMail API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow asks users to run a remote Python script that is not signed or checksum-pinned in the evidence. <br>
Mitigation: Review the downloaded setup script before running it, or ask the publisher for a signed or checksum-pinned installer. <br>
Risk: ClawMail credentials are stored locally in ~/.clawmail/config.json. <br>
Mitigation: Protect the local config file, keep it out of source control and shared logs, and rotate credentials if the file is exposed. <br>
Risk: Agent email may contain untrusted content or sensitive data. <br>
Mitigation: Use a dedicated low-risk inbox, validate senders before processing email content, and avoid sending secrets or regulated data unless approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heyarviind/skills/clawmail) <br>
- [ClawMail website](https://clawmail.cc) <br>
- [ClawMail API documentation](https://clawmail.cc/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples, shell commands, JSON configuration, and Python helper code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CLAWMAIL_SYSTEM_ID or credentials stored in ~/.clawmail/config.json for ClawMail API requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
