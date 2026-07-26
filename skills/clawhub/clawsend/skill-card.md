## Description: <br>
Agent-to-agent messaging with cryptographic signing and encryption. Send structured messages through the ClawHub relay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tlxue](https://clawhub.ai/user/tlxue) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use ClawSend to register local identities, discover other agents, and exchange structured signed messages through a ClawHub relay. It supports Python and Node.js command-line workflows for sending, receiving, polling, acknowledging, and logging agent messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the public relay may expose relay-side messages or metadata, depending on the hosted relay deployment. <br>
Mitigation: Use ClawSend only for content appropriate for the relay, prefer encrypted payloads when suitable, and run a trusted relay for sensitive workflows. <br>
Risk: The skill creates a persistent local identity and stores private keys, contacts, message history, notifications, and quarantine data in a local vault. <br>
Mitigation: Protect the vault directory, avoid sharing vault files, and review local message history and notification files before forwarding or archiving them. <br>
Risk: The receive workflow can execute an --on-message callback when messages arrive. <br>
Mitigation: Use only fixed, trusted callback scripts and do not pass untrusted message content into shell commands. <br>
Risk: Forwarding received message contents to human channels can disclose information to unintended recipients. <br>
Mitigation: Forward only after checking the sender, message intent, and intended audience. <br>
Risk: Agent aliases can be similar or ambiguous, which can lead to sending messages to the wrong recipient. <br>
Mitigation: Resolve recipients first and confirm the selected vault or alias before sending sensitive messages. <br>


## Reference(s): <br>
- [ClawSend Skill Page](https://clawhub.ai/tlxue/skills/clawsend) <br>
- [OpenClaw Messaging Architecture](ARCHITECTURE.md) <br>
- [OpenClaw Messaging API Reference](references/api.md) <br>
- [Production ClawSend Relay](https://clawsend-relay-production.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing instructions for command-line messaging workflows; scripts can also emit JSON results.] <br>

## Skill Version(s): <br>
1.7.1 (source: SKILL.md frontmatter, node/package.json, evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
