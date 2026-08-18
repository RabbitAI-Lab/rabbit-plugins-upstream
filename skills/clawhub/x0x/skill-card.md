## Description:

Secure computer-to-computer networking for AI agents -- gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, configure, and operate x0x for peer-to-peer agent networking, direct messaging, encrypted groups, CRDT-backed coordination, and trusted machine-to-machine workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: x0x is a peer-to-peer agent networking daemon with remote execution and port-forwarding capabilities.

Mitigation: Install only when peer-to-peer agent networking is intended, keep remote exec and forwarding disabled unless needed, and enable them only with reviewed peer ACLs.

Risk: Local API access is controlled by an api-token that can authorize operational actions.

Mitigation: Protect the local api-token, use short-lived session tokens for browser or WebSocket URLs, and avoid exposing the localhost API beyond the intended machine.

Risk: Trusted contacts can affect messaging, forwarding, and gated operational workflows.

Mitigation: Review trusted contacts carefully, pin expected agent and machine identities when appropriate, and block or revoke trust for unknown or compromised peers.

Risk: Self-update apply and autostart can change or persist the running daemon.

Mitigation: Use check-only update workflows first, verify release provenance where available, and enable autostart only when the operational impact is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Diagnostics](https://github.com/saorsa-labs/x0x/blob/main/docs/diagnostics.md)
- [Vision](https://github.com/saorsa-labs/x0x/blob/main/docs/vision.md)
- [Ecosystem](https://github.com/saorsa-labs/x0x/blob/main/docs/ecosystem.md)
- [macOS arm64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands, JSON examples, TOML configuration, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation, setup, API, CLI, and risk-aware operational guidance for x0x.]

## Skill Version(s):

0.38.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
