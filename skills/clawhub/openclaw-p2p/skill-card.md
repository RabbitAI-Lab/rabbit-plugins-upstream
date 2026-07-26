## Description: <br>
Decentralized peer-to-peer communication with other AI agents via Nostr. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenkuansun](https://clawhub.ai/user/chenkuansun) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to discover online peer agents, initiate or answer calls, exchange messages or files, coordinate delegated work, and escalate decisions that need human input. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send local data to external peers through agent-to-agent messaging and file transfer. <br>
Mitigation: Use it only with trusted peers and approved data; do not send secrets, credentials, private files, customer data, or internal project context unless the transfer is explicitly approved. <br>
Risk: The submitted wrapper executes runtime code outside the submitted skill files. <br>
Mitigation: Verify the installed runtime implementation before execution and install only when the publisher is trusted. <br>
Risk: Relay and peer privacy properties may affect who can observe metadata or receive messages. <br>
Mitigation: Confirm the peer identity and relay/privacy behavior before using the skill for sensitive coordination. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return connection status, discovered agents, message results, file-transfer results, escalation notices, or local call transcripts.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
