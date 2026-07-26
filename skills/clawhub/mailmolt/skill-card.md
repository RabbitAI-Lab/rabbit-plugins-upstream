## Description: <br>
Provides an AI agent with its own email address to send, receive, search, and manage emails independently under human supervision. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rakesh1002](https://clawhub.ai/user/rakesh1002) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use MailMolt to give an AI agent a separate email identity for inbox checks, email search, sending and replying with oversight, and communication with humans or other agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad email triggers and direct outbound email handlers can cause unintended email access or sending. <br>
Mitigation: Keep outbound approval controls enabled, use the lowest permission level that meets the task, and review recipients and message content before sending. <br>
Risk: Agent email use can expose credentials, private documents, or sensitive operational details. <br>
Mitigation: Do not allow the agent to email sensitive material unless the exact recipient and content are explicitly approved. <br>
Risk: Automatic read marking can change unread state before a human reviews messages. <br>
Mitigation: Disable auto_mark_read when unread state matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rakesh1002/skills/mailmolt) <br>
- [MailMolt homepage](https://mailmolt.com) <br>
- [MailMolt documentation](https://mailmolt.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with plain text agent responses and JSON or shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a MailMolt API key and network access to api.mailmolt.com; can operate the agent's MailMolt inbox, search messages, and propose or send email according to configured approvals.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
