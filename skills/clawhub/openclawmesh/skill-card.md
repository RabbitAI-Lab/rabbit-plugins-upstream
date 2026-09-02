## Description:

Connect OpenClaw to local and LAN P2P AI agent meshes (JarvisMesh & OpenClawMesh) with explicit user consent for network access, remote delegation, key-file access, and tool exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to connect OpenClaw agents into a peer-to-peer AI mesh for peer discovery, remote task delegation, distributed inference, streaming responses, vector memory, and exposing selected local tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate as a full P2P/WAN-capable AI mesh and gateway, which may expose services more broadly than expected.

Mitigation: Install it only when that network posture is intended, keep services bound to 127.0.0.1 unless broader access is needed, and review gateway or daemon settings before enabling them.

Risk: WAN, DHT, UPnP, QUIC, and GossipSub features can increase network reachability and data movement.

Mitigation: Disable these features unless explicitly required and enable them only after confirming peer identity, network scope, and operator consent.

Risk: Remote delegation may transmit prompts, files, memory, media, and tool results to selected peers.

Mitigation: Use PSK or TrustStore authentication, avoid sending sensitive data to untrusted peers, and review delegated payloads before execution.

Risk: Documentation badges may imply verification beyond what server evidence proves.

Mitigation: Treat server-resolved metadata and scan output as authoritative and do not rely on badge text as proof of ClawHub approval.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/samajesteduroyaume/OpenClawMesh)
- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [README](README.md)
- [User Manual](docs/MANUAL.md)
- [Architecture](ARCHITECTURE.md)
- [Whitepaper](WHITEPAPER.md)
- [Protocol Specification](references/PROTOCOL_SPEC.md)
- [Security Model](references/SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell, Python, JSON, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause an agent to propose network, gateway, daemon, key-management, and deployment commands that require operator review before execution.]

## Skill Version(s):

0.1.22 (source: ClawHub release metadata; artifact frontmatter is 1.1.0 and pyproject.toml is 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
