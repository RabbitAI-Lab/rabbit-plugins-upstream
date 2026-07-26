## Description: <br>
Encrypted peer-to-peer messaging for OpenClaw agents across machines with direct connections, multi-identity support, and native wake support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexrudloff](https://clawhub.ai/user/alexrudloff) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to set up encrypted peer-to-peer communication between OpenClaw agents on different machines or networks, including daemon setup, peer management, message sending, and wake-on-message integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A network-reachable P2P daemon can receive messages from remote peers and may trigger local OpenClaw events with raw message text. <br>
Mitigation: Run the daemon only for trusted agent networks, disable OpenClaw wake unless required, and restrict remote peers to explicit trusted principals. <br>
Risk: Example scripts and command snippets include simple passwords, command-line credentials, and sample workflow paths. <br>
Mitigation: Replace examples with secure password files or secret management, protect credential files, and adapt paths and polling workflows before production use. <br>
Risk: Poll, watcher, and wake examples can forward or process received message content without sanitization or rate controls. <br>
Mitigation: Add sanitization, consent checks, logging, and rate limits before reusing those examples in deployed agents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexrudloff/skills/clawchat-p2p) <br>
- [README](artifact/README.md) <br>
- [Quick Start](artifact/QUICKSTART.md) <br>
- [Full Reference](artifact/REFERENCE.md) <br>
- [OpenClaw Integration Recipes](artifact/skills/clawchat/RECIPES.md) <br>
- [OpenClaw Integration Guide](artifact/skills/clawchat/OPENCLAW-INTEGRATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include daemon setup steps, peer configuration, OpenClaw wake settings, and messaging patterns.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
