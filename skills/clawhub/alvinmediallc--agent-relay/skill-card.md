## Description: <br>
Bridge between an AI agent and a phone for sending and receiving messages with attachments and push notifications, using push-first webhooks with polling fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alvinmediallc](https://clawhub.ai/user/alvinmediallc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an AI agent to a phone workflow, allowing the agent to receive phone-originated messages and attachments, send replies, and issue push notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Phone messages and attachments can pass through the relay service into an agent session. <br>
Mitigation: Install only when this behavior is intended, use a trusted relay URL and credentials, and avoid sending secrets through messages or notifications. <br>
Risk: A public webhook can wake an agent with broad tools if endpoint authentication or routing is weak. <br>
Mitigation: Require a strong webhook secret or equivalent validation before requests reach OpenClaw, restrict the public endpoint, and use a separate bearer token for hooks. <br>
Risk: Attachment downloads can consume local storage or expose the agent to untrusted files. <br>
Mitigation: Set attachment storage limits, store files in a controlled directory, and review attachments before using them in sensitive workflows. <br>
Risk: Polling fallback can repeatedly process queued messages if it is enabled unnecessarily or deduplication state is lost. <br>
Mitigation: Keep cron polling disabled unless fallback delivery is needed and preserve the poller's last-seen state. <br>


## Reference(s): <br>
- [Agent Relay API Reference](references/RELAY_API.md) <br>
- [OpenClaw Hooks Configuration](references/hooks-config.md) <br>
- [Attachment Transform](references/transform.mjs) <br>
- [ClawHub Skill Page](https://clawhub.ai/alvinmediallc/skills/agent-relay) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON snippets, and script references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses relay credentials and may pass phone messages or attachments into an agent session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
