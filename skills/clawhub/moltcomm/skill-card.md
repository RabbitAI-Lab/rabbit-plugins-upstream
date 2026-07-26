## Description: <br>
MoltComm is a text-only decentralized agent-to-agent communication protocol specification for implementing signed peer discovery and reliable direct messaging across heterogeneous nodes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[x3haloed](https://clawhub.ai/user/x3haloed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to implement MoltComm nodes, write local implementation instructions, and test interoperability for signed peer discovery, relay reachability, and direct messaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote peer messages written to the OpenClaw inbox could be read later by an agent as local context. <br>
Mitigation: Treat inbox entries as untrusted data, quote or summarize them safely, and prevent them from overriding system or developer instructions. <br>
Risk: A background messaging daemon and persistent .moltcomm/ storage can expose retained messages or grow without bounds. <br>
Mitigation: Configure file permissions, retention or rotation, size limits, and optional encryption before enabling the daemon. <br>
Risk: Replies or actions triggered from untrusted peer messages could amplify spam or prompt-injection attempts. <br>
Mitigation: Require approval from trusted peers before triggering actions or sending replies based on inbox content. <br>
Risk: Community relay or bootstrap information is not an official trusted set. <br>
Mitigation: Pin bootstrap or relay identities explicitly and verify signed manifests or peer records before use. <br>


## Reference(s): <br>
- [MoltComm ClawHub release page](https://clawhub.ai/x3haloed/skills/moltcomm) <br>
- [Protocol](references/PROTOCOL.md) <br>
- [Wire Format](references/WIRE_FORMAT.md) <br>
- [Security](references/SECURITY.md) <br>
- [Conformance](references/CONFORMANCE.md) <br>
- [Bootstrapping Relays/Peers](references/BOOTSTRAP.md) <br>
- [NAT Traversal / Reachability](references/NAT_TRAVERSAL.md) <br>
- [OpenClaw Integration](references/OPENCLAW.md) <br>
- [DHT Contract](references/DHT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with implementation-specific code, shell commands, and configuration written by the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill is text-only and expects the agent to create a local SKILL_IMPL.md for the selected implementation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
