## Description: <br>
Send emails via SMTP using configured environment credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to send SMTP email messages, optionally with a local file attachment, after SMTP credentials are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send arbitrary email content to external recipients. <br>
Mitigation: Verify the recipient, subject, and body with the user before execution, and avoid unattended bulk automation. <br>
Risk: Attachment support can disclose sensitive local files or private context. <br>
Mitigation: Require explicit approval for each attachment path and confirm the file is intended to be shared. <br>


## Reference(s): <br>
- [Send Email skill on ClawHub](https://clawhub.ai/legionspace-hackathon/skills/send-email) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, text] <br>
**Output Format:** [Command-line invocation with text status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SMTP environment variables and supports an optional attachment path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
