## Description:

Secure computer-to-computer networking for AI agents -- gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encrypted transport, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to install, configure, and operate x0x as a local P2P networking daemon for AI agents. It supports direct messages, gossip pub/sub, encrypted groups, CRDT-backed task and store workflows, file transfer, diagnostics, and trust-gated forwarding or remote execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running x0x starts a local P2P networking daemon with agent communication and networking capabilities.

Mitigation: Install it only when you intend to operate a local P2P daemon, review its configuration, and keep autostart disabled unless continuous operation is needed.

Risk: The local api-token can authorize daemon operations if exposed.

Mitigation: Protect the api-token, avoid placing durable tokens in URLs, and use short-lived session tokens for browser or WebSocket access.

Risk: Forwarding and remote execution are powerful features even when gated.

Mitigation: Enable forwarding or remote exec only after reviewing trust and ACL settings, and allow only expected peers, machines, and command arguments.

Risk: Release downloads use latest-version URLs that may not satisfy stricter supply-chain controls.

Mitigation: Prefer verified or pinned releases where the deployment environment requires stronger release integrity controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Project Repository](https://github.com/saorsa-labs/x0x)
- [Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Diagnostics](https://github.com/saorsa-labs/x0x/blob/main/docs/diagnostics.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [macOS ARM64 Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux ARM64 GNU Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, TOML configuration, and REST/WebSocket usage patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for installing binaries or building from source, starting the daemon, calling local APIs, configuring trust controls, and operating diagnostics.]

## Skill Version(s):

0.36.1 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
