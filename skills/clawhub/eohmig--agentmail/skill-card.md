## Description: <br>
AgentMail helps AI agents create and manage dedicated inboxes, send and receive email programmatically, and automate email workflows with webhooks and real-time events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to give agents email identities, send status updates or attachments, inspect inboxes and threads, and automate inbound email workflows through webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an AgentMail API key that can permit agents to send, receive, and process email. <br>
Mitigation: Install only when that access is intended, scope and rotate the API key where possible, and avoid placing secrets in prompts, logs, or shared output. <br>
Risk: Incoming email and webhook payloads can contain untrusted content, including prompt-injection attempts. <br>
Mitigation: Use sender allowlists, restrict webhook event types and inbox filters, mark email bodies as untrusted input, and review untrusted messages in an isolated session before agent action. <br>
Risk: Webhook examples and local test servers can expose email data or development endpoints if published carelessly. <br>
Mitigation: Authenticate webhook endpoints, verify webhook signatures in production, avoid exposing local test servers unnecessarily, and redact or review email content before forwarding it to GitHub, logs, or third parties. <br>


## Reference(s): <br>
- [AgentMail API Reference](references/API.md) <br>
- [AgentMail Webhooks Guide](references/WEBHOOKS.md) <br>
- [AgentMail Usage Examples](references/EXAMPLES.md) <br>
- [AgentMail API endpoint](https://api.agentmail.to/v0) <br>
- [AgentMail Console](https://console.agentmail.to) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown guidance with Python, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes optional Python scripts for sending email, checking inboxes, and managing webhooks; script use requires AGENTMAIL_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
