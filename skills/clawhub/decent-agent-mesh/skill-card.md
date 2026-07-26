## Description: <br>
Agent Mesh lets agents on different machines send and receive messages over the Decent Network peer-to-peer mesh without a third-party platform, server, or account registration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xli](https://clawhub.ai/user/0xli) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Agent Mesh to create a peer-to-peer messaging channel between agent roles on different machines. It is intended for agent-to-agent coordination where users want keypair identity, a mutual friend handshake, and no third-party chat or webhook account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mesh sends, friend requests, and inbox contents are external network communication over a peer-to-peer channel. <br>
Mitigation: Do not send credentials or private files, and review peers before accepting or allow-listing them. <br>
Risk: The skill relies on an always-on daemon, public DHT connectivity, and an npm dependency for delivery. <br>
Mitigation: Supervise the daemon, verify status freshness and round-trip delivery before relying on the channel, and pin dependencies when reproducible installs are required. <br>


## Reference(s): <br>
- [Agent Mesh ClawHub Page](https://clawhub.ai/0xli/skills/decent-agent-mesh) <br>
- [Decent Network](https://decent.network) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, npm, AGENT_NAME, and an internet connection for the peer-to-peer mesh.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
