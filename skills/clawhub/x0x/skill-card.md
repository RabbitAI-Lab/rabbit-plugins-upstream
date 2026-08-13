## Description:

Secure computer-to-computer networking for AI agents: gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

Developers and agent builders use this skill to install, configure, and operate x0x as a decentralized networking layer for agent messaging, replicated state, group encryption, task coordination, port forwarding, and trust-gated peer operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and operates an agent networking daemon with high-risk features including remote exec, port forwarding, autostart, and self-update.

Mitigation: Install only when an agent networking daemon is intended; enable autostart or self-update only when comfortable with the release source.

Risk: The local API token grants access to non-public daemon routes.

Mitigation: Treat the API token like a password and avoid exposing durable tokens in URLs; use short-lived session tokens where documented.

Risk: Port forwarding can expose sensitive local services if configured carelessly.

Mitigation: Review trust and connect ACL settings before enabling forwarding, and avoid forwarding sensitive local services such as SSH unless that is intended.

Risk: Remote command execution can affect peer machines when enabled.

Mitigation: Keep remote exec disabled unless needed, require trusted contacts, and use exact argv allow-lists as documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x homepage](https://saorsalabs.com)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [macOS arm64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, curl examples, JSON examples, and TOML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes installation commands, daemon operations, REST and WebSocket examples, trust and ACL guidance, and configuration snippets.]

## Skill Version(s):

0.37.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
