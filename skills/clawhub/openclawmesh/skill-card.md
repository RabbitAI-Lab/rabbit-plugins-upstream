## Description:

Connect OpenClaw to local and LAN P2P AI agent meshes (JarvisMesh & OpenClawMesh). Requires explicit user consent for mDNS, LAN/WAN network access, remote delegation, key-file access, and exposing local tools. Remote traffic may transmit prompts, files, memory, media, and tool results to selected peers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use Openclaw Mesh to discover peer AI nodes, delegate inference or tool calls across local and WAN meshes, stream responses, and share memory or multimodal workloads across heterogeneous hardware.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mesh features can enable broad WAN networking, external registration, peer discovery, and sharing of prompts, files, memory queries, media, IP details, and advertised skills.

Mitigation: Install only on machines intended to participate in a P2P AI mesh, keep WAN/Guichet/DHT/UPnP/mDNS disabled unless needed, and use PSK or TrustStore authentication before sending sensitive workloads.

Risk: Optional daemon or service installation can add boot persistence.

Mitigation: Review the generated service file and operating-system startup behavior before using the daemon installer.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/samajesteduroyaume/OpenClawMesh)
- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Protocol specification](references/PROTOCOL_SPEC.md)
- [Security model](references/SECURITY_MODEL.md)
- [User manual](docs/MANUAL.md)
- [Architecture](ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands and configuration that enable local or WAN mesh networking when the operator opts in.]

## Skill Version(s):

0.1.24 (source: ClawHub release metadata; artifact versions: SKILL.md 1.1.0, pyproject.toml 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
