## Description:

Connects OpenClaw agents to local and opt-in LAN or WAN peer-to-peer AI meshes for discovery, remote delegation, streaming, memory, multimodal tasks, and exposing selected local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use Openclaw Mesh to connect OpenClaw agents into local or explicitly enabled WAN peer meshes for distributed inference, peer discovery, vector memory/RAG, multimodal workflows, and remote tool exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates as a network service and remote execution gateway, so exposed peers or gateway endpoints can transmit prompts, files, memory, media, and tool results outside the local machine.

Mitigation: Keep services bound to localhost unless WAN access is intentional, require strong PSK or trusted identity credentials, and review selected peers and exposed skills before delegation.

Risk: Docker or service modes may expose listeners broadly if configured with 0.0.0.0 or WAN options.

Mitigation: Avoid broad bind addresses by default, enable TLS plus PSK or a TrustStore for any external access, and disable QUIC, DHT, STUN, relay, and gateway features unless they have been explicitly reviewed.

Risk: Advertised PQC, TEE, sandbox, and encryption capabilities do not remove the need to review sensitive-data handling.

Mitigation: Do not rely on those claims alone for sensitive data; verify configuration, peer identity, authentication mode, and the actual data sent to remote peers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Server-Resolved Source Repository](https://github.com/samajesteduroyaume/OpenClawMesh)
- [README](README.md)
- [User Manual](docs/MANUAL.md)
- [Architecture](ARCHITECTURE.md)
- [Whitepaper](WHITEPAPER.md)
- [Protocol Specification](references/PROTOCOL_SPEC.md)
- [Security Model](references/SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payloads, and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include peer addresses, skill payloads, environment variables, authentication options, and operator consent steps.]

## Skill Version(s):

0.1.21 (source: ClawHub release metadata; artifact sources include SKILL.md 1.1.0 and pyproject.toml 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
