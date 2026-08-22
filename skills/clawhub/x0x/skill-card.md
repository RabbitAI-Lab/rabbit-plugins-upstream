## Description:

Secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

Developers and agent builders use x0x to set up peer-to-peer networking, messaging, shared CRDT state, encrypted groups, local REST/WebSocket agent communication, and optional trusted machine-to-machine operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: x0x runs a long-running peer-to-peer agent networking daemon.

Mitigation: Install it only when persistent peer-to-peer agent networking is intended, and review the trusted release source before deployment.

Risk: The local REST/WebSocket API uses an api-token that can authorize privileged local operations.

Mitigation: Protect the local api-token, avoid putting durable tokens in URLs, and use short-lived session tokens where the skill documentation specifies them.

Risk: Autostart, port forwarding, self-update, and remote exec can expand operational impact if enabled casually.

Mitigation: Enable these features deliberately, keep remote exec disabled unless needed, and restrict remote exec ACLs to exact commands for trusted peers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [macOS arm64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and TOML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for binary installation paths; the tool installs x0xd and x0x binaries when used through OpenClaw metadata.]

## Skill Version(s):

0.39.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
