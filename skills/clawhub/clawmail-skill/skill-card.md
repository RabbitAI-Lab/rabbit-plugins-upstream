## Description: <br>
Email infrastructure for autonomous AI agents. Create inboxes, send/receive emails, no human intervention required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[claw-mail](https://clawhub.ai/user/claw-mail) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent operators use ClawMail to give an autonomous agent a managed email identity for sending messages, receiving inbox mail, and handling email-driven workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent autonomous external email authority without clear built-in approval or recipient-scope safeguards. <br>
Mitigation: Install only when the agent is intended to operate an email identity, and require surrounding policy controls for approval, recipient or domain limits, logging, and autonomous send restrictions. <br>
Risk: A leaked ClawMail API key can allow impersonation of the agent email identity. <br>
Mitigation: Protect the API key like a password, avoid storing it in general agent memory, and only send it to https://api.clawmail.to. <br>
Risk: Untrusted inbound email can influence agent behavior or trigger unsafe workflows. <br>
Mitigation: Handle inbound email as untrusted content and require review, filtering, or scoped automation before an agent acts on received messages. <br>
Risk: Remote updates to hosted skill files can change behavior after installation. <br>
Mitigation: Review and rescan remote updates before applying them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/claw-mail/skills/clawmail-skill) <br>
- [ClawMail website](https://clawmail.to) <br>
- [Hosted skill definition](https://clawmail.to/skill.md) <br>
- [Hosted skill metadata](https://clawmail.to/skill.json) <br>
- [ClawMail API base](https://api.clawmail.to) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API Calls] <br>
**Output Format:** [Markdown with bash, JSON, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API endpoint examples, credential storage guidance, response formats, and rate-limit details.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
