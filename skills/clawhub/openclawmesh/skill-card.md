## Description:

Openclaw Mesh connects OpenClaw to P2P AI agent meshes for peer discovery, remote delegation, hardware-aware inference, streaming, memory, multimodal tasks, and optional tool exposure, with explicit consent required before network, key-file, or remote-sharing operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT License with Commercial Services Addendum

## Use Case:

Developers and agent operators use Openclaw Mesh to discover peer AI nodes, delegate inference and memory tasks, stream responses, inspect hardware, and optionally expose local OpenClaw tools across LAN or explicitly enabled WAN mesh connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose P2P serving, WAN, DHT, relay, and gateway capabilities that may share prompts, files, media, memory queries, and tool results outside the local machine.

Mitigation: Enable these capabilities only after explicit consent, use strong PSK or TrustStore controls, and apply TLS for any non-local exposure.

Risk: The optional Bitcoin payment and admin gateway is broader than a small mesh connector and is not clearly declared in the main skill manifest.

Mitigation: Install only when the full P2P mesh package is desired, keep the gateway bound to localhost unless separately hardened, and override wallet and admin token settings before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Server-resolved GitHub repository](https://github.com/samajesteduroyaume/OpenClawMesh)
- [Architecture](ARCHITECTURE.md)
- [Protocol Specification](references/PROTOCOL_SPEC.md)
- [Security Model](references/SECURITY_MODEL.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, JSON payloads, and peer response text or structured status data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream token responses and may include remote peer results when delegation is explicitly enabled.]

## Skill Version(s):

0.1.10 (source: server release metadata; artifact frontmatter and pyproject.toml state 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
