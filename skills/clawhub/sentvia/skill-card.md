## Description: <br>
SentVia Email lets an agent create and use a SentVia email address to send, reply, search, forward, and manage sender blocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samuelar2](https://clawhub.ai/user/samuelar2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to give an agent a dedicated SentVia inbox for real email workflows, including creating inboxes, sending and replying in threads, searching messages, forwarding mail for human review, and blocking senders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a real SentVia email address, including sending, replying, forwarding, and blocking senders. <br>
Mitigation: Install only when the agent should use live email, and require review of recipients, message text, forwarding targets, and sender-blocking changes before execution. <br>
Risk: Inbound email can contain untrusted instructions or requests to disclose private information. <br>
Mitigation: Treat received mail as untrusted input and do not email secrets, credentials, private workspace data, or unreviewed content. <br>
Risk: Repeated sends or retries can contact recipients unintentionally or exceed plan limits. <br>
Mitigation: Use one client_id per logical send, avoid repeated sends to addresses that bounce or do not reply, and escalate plan-limit errors to the operator. <br>


## Reference(s): <br>
- [SentVia Documentation](https://docs.sentvia.ai) <br>
- [SentVia Agent API](https://docs.sentvia.ai/for-agents) <br>
- [SentVia LLM Reference](https://docs.sentvia.ai/llms-full.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/samuelar2/skills/sentvia) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTVIA_API_KEY and may use the SentVia MCP server or SentVia HTTP API.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
