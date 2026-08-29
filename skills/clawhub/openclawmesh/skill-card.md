## Description:

Connect OpenClaw to local and LAN P2P AI agent meshes for peer discovery, remote delegation, hardware-aware inference, memory, multimodal tasks, and optional WAN routing with explicit user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to connect OpenClaw agents to local or selected remote mesh peers for task delegation, streaming inference, vector memory, hardware discovery, and exposing local tools. It is most appropriate when the operator intends to run a networked P2P agent or gateway and can manage peer trust, keys, and network exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run networked P2P agent and gateway features that may expose prompts, files, memory, media, tool results, admin tokens, or shared cache data.

Mitigation: Install only when this networked behavior is intended, keep WAN, DHT, relay, STUN, and UPnP disabled unless needed, and bind services to localhost by default.

Risk: Remote delegation and shared gateways can transmit sensitive data to selected peers.

Mitigation: Avoid sending sensitive prompts or files through shared gateways, verify peer identity before delegation, and use strong PSKs or TrustStores.

Risk: Gateway admin tokens may be exposed if retained in untrusted browser contexts.

Mitigation: Do not persist admin tokens in the portal on untrusted browsers, and rotate tokens if exposure is suspected.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/samajesteduroyaume/OpenClawMesh)
- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Protocol specification](references/PROTOCOL_SPEC.md)
- [Security model](references/SECURITY_MODEL.md)
- [Architecture](ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate network and gateway commands that require operator consent and local configuration before execution.]

## Skill Version(s):

0.1.15 (source: server release metadata; artifact frontmatter and pyproject.toml report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
