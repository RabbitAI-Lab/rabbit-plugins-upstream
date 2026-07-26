## Description: <br>
Guides an agent and user through sending SMTP email with MGC-stored credentials and scripts so credentials are not exposed to the agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure an agent-assisted SMTP workflow where the user stores credentials and scripts in MGC, reviews recipient, subject, and body, and authorizes each send. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead to outbound email being sent through locally stored SMTP credentials. <br>
Mitigation: Require explicit user approval for every send after reviewing the recipient, subject, and body. <br>
Risk: Stored MGC scripts can read local MGC secrets and execute email-sending behavior hidden from the agent. <br>
Mitigation: Review and trust the stored script contents before installation or execution, and only use credential names after confirming the local MGC setup. <br>
Risk: The release under-discloses that runnable code can read local MGC secrets and send email. <br>
Mitigation: Treat the skill as active email-sending guidance rather than passive documentation and apply local security review before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/smtp-sender-secure) <br>
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox) <br>
- [MGC Blackbox Issues](https://github.com/zkeviny/MGC-Blackbox/issues) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with Python snippets, JSON examples, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-controlled MGC credential storage and explicit review before email sending.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
