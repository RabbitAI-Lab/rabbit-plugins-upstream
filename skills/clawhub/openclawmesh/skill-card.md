## Description:

Connect OpenClaw to local and LAN P2P AI agent meshes (JarvisMesh & OpenClawMesh) to discover peer nodes, delegate tasks across multiple hardware architectures, run multimodal and memory workflows, stream responses, and expose local tools to the decentralized network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT License with Commercial Services Addendum

## Use Case:

Developers and engineers use this skill to connect OpenClaw agents into peer-to-peer meshes for local or WAN discovery, task delegation, streaming inference, vector-memory access, multimodal processing, and exposing local tools to other mesh peers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-facing serve, relay, and gateway endpoints can expose mesh capabilities beyond the intended host or trusted network.

Mitigation: Bind endpoints to localhost or a trusted interface unless explicitly hardened, and require PSK or a trust store before accepting peer requests.

Risk: Automatic delegation can send sensitive prompts, files, images, or audio to discovered peers.

Mitigation: Avoid auto-delegating sensitive data; prefer trusted target peers and review payloads before forwarding them across the mesh.

Risk: Gateway deployment has unresolved concerns around demo or simulated key endpoints, default admin token behavior, webhook verification, and API-key handling.

Mitigation: Do not deploy the gateway until those gateway controls are fixed and reviewed.

## Reference(s):

- [OpenClawMesh GitHub Repository](https://github.com/samajesteduroyaume/OpenClawMesh)
- [Openclaw Mesh ClawHub Listing](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Protocol Specification](references/PROTOCOL_SPEC.md)
- [Security Model](references/SECURITY_MODEL.md)
- [Python Downloads](https://www.python.org/downloads/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that start mesh services, discover peers, delegate tasks, stream model output, manage keys, or configure authentication.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter and pyproject.toml list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
