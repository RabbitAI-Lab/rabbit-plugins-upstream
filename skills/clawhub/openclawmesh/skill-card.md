## Description:

Openclaw Mesh connects OpenClaw agents to local and LAN/WAN P2P AI meshes for peer discovery, remote task delegation, and tool sharing, with sensitive prompts, files, memory, media, and tool results potentially sent to selected peers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Openclaw Mesh to discover AI peers, delegate inference or retrieval tasks across a P2P mesh, and expose selected local tools to trusted nodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports broad network exposure and optional startup persistence that are not fully aligned with opt-in permission claims.

Mitigation: Review before installing, and use the skill only when the operator intends to run a P2P network service.

Risk: Mesh operation can share prompts, files, memory, media, tool results, host identity, and network addresses with peers or rendezvous services.

Mitigation: Set a strong PSK or TrustStore, confirm what data may be shared, and disable WAN, DHT, UPnP, and Freebox registration unless they are needed.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/samajesteduroyaume/OpenClawMesh)
- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Protocol specification](references/PROTOCOL_SPEC.md)
- [Security model](references/SECURITY_MODEL.md)
- [User manual](docs/MANUAL.md)
- [Architecture](ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include peer-discovery, network, security, and deployment instructions for running a P2P AI mesh.]

## Skill Version(s):

0.1.23 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0 and pyproject.toml reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
