## Description:

Secure computer-to-computer networking for AI agents - gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and operate x0x as a peer networking layer for AI agents, including direct messaging, gossip pub/sub, encrypted groups, CRDT-backed task and key-value stores, file transfer, and tailnet-style port forwarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill bundles and operates a peer networking daemon.

Mitigation: Install only when peer networking is intended, start the daemon explicitly, and avoid autostart unless continuous operation is required.

Risk: Remote command execution can run commands on peer machines.

Mitigation: Keep remote exec disabled unless exact peer identities and command allowlists are configured and reviewed.

Risk: Port forwarding can expose sensitive loopback services to trusted peers.

Mitigation: Forward only explicitly approved loopback targets and review connect ACLs before enabling forwards.

Risk: The local API token controls privileged daemon operations.

Mitigation: Protect the local api-token file and avoid placing durable tokens in URLs or logs.

Risk: Self-update can replace installed binaries.

Mitigation: Review the self-update flow before allowing an agent to check for or apply updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [macOS arm64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Diagnostics](https://github.com/saorsa-labs/x0x/blob/main/docs/diagnostics.md)
- [Remote Exec](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls, Markdown]

**Output Format:** [Markdown with shell commands, JSON request examples, and TOML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation, daemon operation, API usage, trust, networking, diagnostics, and update guidance for x0x.]

## Skill Version(s):

0.37.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
