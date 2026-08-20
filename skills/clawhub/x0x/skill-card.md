## Description:

Secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use x0x to install and operate a peer-to-peer networking daemon for agent discovery, direct and group messaging, replicated task and key-value state, file transfer, gated port forwarding, and gated remote execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a peer-to-peer networking daemon with powerful networking features.

Mitigation: Install only when a peer-to-peer agent network is intended, keep the local API token protected, and avoid autostart unless persistent operation is required.

Risk: The release installs downloaded binaries and server-resolved provenance is unavailable for this version.

Mitigation: Review the source or release provenance before trusting the binaries, and prefer verified install paths when available.

Risk: Port forwarding and remote execution can affect local or peer systems if enabled too broadly.

Mitigation: Enable forwarding or remote execution only for trusted peers and exact commands or targets that are intentionally allowed.

## Reference(s):

- [ClawHub x0x Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x Repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code, API Calls]

**Output Format:** [Markdown with shell, TOML, JSON, REST, and WebSocket examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform-specific binary installation guidance, daemon configuration, CLI commands, and local API usage examples.]

## Skill Version(s):

0.38.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
