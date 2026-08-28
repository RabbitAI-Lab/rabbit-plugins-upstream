## Description:

Connects OpenClaw to local and LAN P2P AI agent meshes for peer discovery, remote task delegation, hardware-aware inference, streaming, memory/RAG, multimodal tasks, and optional gateway or WAN operation with explicit consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Openclaw Mesh to connect OpenClaw agents to local or LAN P2P mesh nodes for discovering peers, delegating AI tasks, streaming responses, sharing vector memory, and exposing local tools. Optional WAN and gateway features support broader mesh deployments when deliberately configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional gateway and WAN admin features can expose mesh controls beyond the local machine.

Mitigation: Keep the gateway bound to localhost unless intentionally deployed behind hardened TLS and authentication.

Risk: Gateway admin tokens, generated PSKs, browser-stored tokens, and TrustStore material are credentials that can persist or be reused.

Mitigation: Set a strong GATEWAY_ADMIN_TOKEN and PSK or TrustStore, protect configured key paths, and rotate secrets if exposure is suspected.

Risk: Remote delegation can send prompts, files, memory, media, and tool results to selected peers.

Mitigation: Use remote peers only when needed, verify peer identity and permissions, and avoid sending sensitive data to untrusted peers.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Server-resolved GitHub source](https://github.com/samajesteduroyaume/OpenClawMesh)
- [README](artifact/README.md)
- [Architecture](artifact/ARCHITECTURE.md)
- [Protocol Specification](artifact/references/PROTOCOL_SPEC.md)
- [Security Model](artifact/references/SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide Python-based mesh discovery, WebSocket calls, optional DHT/STUN/WAN relay use, local gateway use, and key or TrustStore configuration after user consent.]

## Skill Version(s):

0.1.14 (source: ClawHub release metadata; source files report 1.1.0 in SKILL.md and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
