## Description: <br>
Get a FREE email address "you@sendclaw.com" - Email for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jononovo](https://clawhub.ai/user/jononovo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to give an agent a SendClaw email address, send email through the SendClaw API, check incoming messages, and coordinate replies with human oversight. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent ongoing email-reading and email-sending capability. <br>
Mitigation: Require explicit human approval before sending or replying to external email, and configure CC or dashboard review for important conversations. <br>
Risk: Exposure of SENDCLAW_API_KEY would allow another party to send email as the agent. <br>
Mitigation: Store SENDCLAW_API_KEY in a secrets manager and only use it with SendClaw API requests. <br>
Risk: Checking unread messages can change mailbox state because unread message retrieval auto-marks messages as read. <br>
Mitigation: Use heartbeat polling deliberately, notify the human when quota or unread counts require attention, and avoid autonomous reply loops unless tightly configured. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/jononovo/skills/sendclaw) <br>
- [SendClaw Skill Reference](https://sendclaw.com/SKILL.md) <br>
- [SendClaw Heartbeat Routine](https://sendclaw.com/HEARTBEAT.md) <br>
- [SendClaw Skill Metadata](https://sendclaw.com/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with JSON and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SENDCLAW_API_KEY and the SendClaw API for registration, sending, reading, and optional webhook workflows.] <br>

## Skill Version(s): <br>
1.7.6 (source: server release metadata; artifact frontmatter reports 1.7.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
