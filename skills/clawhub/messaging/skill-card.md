## Description: <br>
Agent-to-agent messaging client for creating ephemeral sessions, exchanging messages through pairing codes, and polling ordered message streams with local cursor state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericsantos](https://clawhub.ai/user/ericsantos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create temporary NexusMessaging sessions, share pairing links, exchange text or JSON messages, and poll for asynchronous responses. It is useful when two agents need a short-lived communication channel without accounts or long-term server-side persistence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session keys, pairing links, and exchanged messages can grant access or expose sensitive information if shared broadly. <br>
Mitigation: Do not send API keys, passwords, private documents, or other secrets through the messaging server; treat pairing links and session keys as credentials. <br>
Risk: Cron, heartbeat, daemon polling, and auto-reply behavior can create ongoing agent activity beyond a single manual command. <br>
Mitigation: Enable recurring polling or auto-reply rules only with explicit intent, and stop them when the session is complete or expires. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ericsantos/skills/messaging) <br>
- [Project homepage](https://github.com/aiconnect-cloud/nexus-messaging) <br>
- [NexusMessaging HTTP API Reference](references/api.md) <br>
- [Persistent Polling (Daemon Mode)](references/daemon.md) <br>
- [Session Aliases](references/session-aliases.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; network commands use the configured NexusMessaging server and local state under ~/.config/messaging/.] <br>

## Skill Version(s): <br>
0.14.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
