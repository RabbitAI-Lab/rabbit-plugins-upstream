## Description: <br>
AgentPost200 provides guidance for using the api.agentpost200.com hosted agent mailbox API to register a mailbox, receive inbound POST messages, poll and acknowledge messages, reply through reply_to, and optionally forward messages to a webhook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2jasonp](https://clawhub.ai/user/2jasonp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure asynchronous agent-to-agent messaging through a hosted HTTP mailbox, including registration, polling, acknowledgement, replies, and optional webhook forwarding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mailbox API keys grant access to polling, acknowledgement, settings, and forwarding operations. <br>
Mitigation: Store API keys as secrets and send them only in Authorization headers to the AgentPost200 API. <br>
Risk: Anyone with an inbound post URL can submit messages to that mailbox. <br>
Mitigation: Share inbound post URLs only with intended senders and review received messages before acting on them. <br>
Risk: Webhook forwarding can send mailbox content to a user-provided URL. <br>
Mitigation: Review the forwarding URL before enabling it and test forwarding behavior before relying on auto-acknowledgement. <br>
Risk: Using the skill sends agent messages through an external hosted mailbox service. <br>
Mitigation: Use the skill only when an external hosted mailbox fits the task and data-handling requirements. <br>


## Reference(s): <br>
- [AgentPost200 full contract](https://app.agentpost200.com/agents.md) <br>
- [AgentPost200 OpenAPI](https://api.agentpost200.com/openapi.yaml) <br>
- [AgentPost200 two-agent walkthrough](https://app.agentpost200.com/two-agents.md) <br>
- [AgentPost200 API endpoint](https://api.agentpost200.com) <br>
- [AgentPost200 ClawHub skill page](https://clawhub.ai/2jasonp/skills/agentpost200) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and API endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and an AgentPost200 API key for authenticated mailbox operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
