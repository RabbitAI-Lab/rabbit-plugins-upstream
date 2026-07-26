## Description: <br>
Agentmail helps agents create and manage dedicated email inboxes, send and receive messages programmatically, and handle email workflows with webhooks and real-time events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rez0](https://clawhub.ai/user/rez0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use Agentmail to give agents email identities, automate sending and receiving messages, poll inboxes, and connect incoming email events to webhook-driven workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incoming email can contain sensitive or untrusted content that may influence automated agent behavior. <br>
Mitigation: Treat email bodies and attachments as untrusted input, review or redact content before forwarding it to other systems, and use sender allowlists for automated actions. <br>
Risk: Webhook endpoints can expose agents to unsolicited email events or spoofed requests if deployed without controls. <br>
Mitigation: Enable webhook signature verification, use HTTPS, restrict webhooks to specific inboxes and event types, and add rate limiting before production use. <br>
Risk: Email-sending automation can disclose information or attachments to unintended recipients. <br>
Mitigation: Validate recipient lists and attachment paths, keep AGENTMAIL_API_KEY secret, and require review for workflows that send externally or forward content to GitHub, Slack, logs, or other third-party systems. <br>


## Reference(s): <br>
- [Agentmail ClawHub page](https://clawhub.ai/rez0/agentmail) <br>
- [AgentMail API Reference](references/API.md) <br>
- [AgentMail Webhooks Guide](references/WEBHOOKS.md) <br>
- [AgentMail Usage Examples](references/EXAMPLES.md) <br>
- [AgentMail Console](https://console.agentmail.to) <br>
- [AgentMail API base URL](https://api.agentmail.to/v0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, configuration snippets, and helper script output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENTMAIL_API_KEY and the AgentMail Python SDK; helper scripts can create webhooks, send email, and inspect inbox messages.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
