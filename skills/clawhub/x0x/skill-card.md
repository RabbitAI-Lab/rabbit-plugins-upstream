## Description:

Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

Developers and agent builders use x0x to set up secure peer-to-peer networking for agent messaging, group communication, shared CRDT-backed state, file transfer, and agent work orchestration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and operates a local peer-to-peer networking daemon for agents.

Mitigation: Install it only when that networking behavior is intended, and review peer connectivity and trust settings before use.

Risk: The local API token can authorize sensitive daemon operations.

Mitigation: Protect the token file and avoid exposing durable tokens in URLs or shared logs.

Risk: Remote execution is a high-risk capability when enabled.

Mitigation: Keep remote exec disabled unless required, and enable it only with explicit peer trust and ACL controls.

Risk: Autostart and self-update can create persistent background service behavior or local binary changes.

Mitigation: Use autostart or self-update only after reviewing the operational impact and update source.

## Reference(s):

- [ClawHub x0x Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [x0x Repository](https://github.com/saorsa-labs/x0x)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [macOS arm64 Release Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 Release Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU Release Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU Release Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 Release Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, API request examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local daemon setup steps, REST/WebSocket examples, trust and ACL guidance, and platform-specific install commands.]

## Skill Version(s):

0.40.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
