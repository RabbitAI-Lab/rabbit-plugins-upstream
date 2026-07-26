## Description: <br>
AgentMail is an API-first email platform for AI agents that helps create dedicated inboxes, send and receive email programmatically, and handle email workflows with webhooks and real-time events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adboio](https://clawhub.ai/user/adboio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use AgentMail to create dedicated agent inboxes, send and receive email programmatically, and connect inbound email workflows to webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles email content, attachments, API keys, and webhook payloads that may include sensitive information. <br>
Mitigation: Keep AGENTMAIL_API_KEY and related tokens secret, avoid logging full payloads in shared systems, and redact or approve email content before forwarding it to GitHub, Slack, or other services. <br>
Risk: Inbound email and webhook events can carry untrusted instructions or prompt-injection attempts. <br>
Mitigation: Restrict webhook endpoints, verify webhook signatures, allowlist trusted senders, and treat email content as untrusted input unless reviewed. <br>
Risk: Forwarding messages or automating replies can expose private data or trigger unintended external communication. <br>
Mitigation: Review outbound message content, scope inboxes and webhook filters narrowly, and require approval before sending sensitive or high-impact messages. <br>


## Reference(s): <br>
- [AgentMail API Reference](references/API.md) <br>
- [AgentMail Webhooks Guide](references/WEBHOOKS.md) <br>
- [AgentMail Usage Examples](references/EXAMPLES.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/adboio/skills/agentmail) <br>
- [Publisher Profile](https://clawhub.ai/user/adboio) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AgentMail API calls, webhook setup steps, inbox polling commands, and email-sending examples.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
