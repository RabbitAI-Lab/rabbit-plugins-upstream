## Description:

Secure computer-to-computer networking for AI agents: gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install, run, configure, and interact with x0x for peer-to-peer agent messaging, encrypted groups, shared CRDT-backed state, file transfer, diagnostics, and controlled automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs native binaries from mutable release URLs.

Mitigation: Use pinned, signature- or checksum-verified release artifacts before installation.

Risk: The skill can run a persistent peer-to-peer daemon with identity keys, bearer-token control, local history, file transfer, self-update, and optional remote execution.

Mitigation: Install only when this daemon behavior is intentional, review update settings, and keep autostart and remote execution disabled unless explicitly needed.

Risk: A non-loopback API binding is protected only by bearer tokens unless separately fronted with TLS.

Mitigation: Keep the API bound to loopback by default, protect the durable api-token like a password, and use TLS if exposing the API beyond localhost.

Risk: Gossip pub/sub payloads are readable by relaying peers.

Mitigation: Treat gossip topics as public and use direct messages or encrypted groups for sensitive content.

Risk: Remote execution is high impact even though it is gated and disabled by default.

Mitigation: Leave remote execution disabled unless explicitly required, and require exact trust and ACL review before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Publisher profile](https://clawhub.ai/user/jimcollinson)
- [Saorsa Labs homepage](https://saorsalabs.com)
- [Security and cryptography documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Remote execution documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade system documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [macOS arm64 release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown with inline shell commands, REST examples, configuration snippets, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational cautions for daemon setup, bearer-token handling, peer trust, remote execution, self-update, and public gossip topics.]

## Skill Version(s):

0.42.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
