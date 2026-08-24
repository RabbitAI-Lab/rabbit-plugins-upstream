## Description:

Secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, and NAT-traversing peer-to-peer connectivity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent builders use this skill to install, configure, and operate x0x for secure peer-to-peer agent communication, task orchestration, encrypted groups, port forwarding, and local REST/WebSocket integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation and operation of a local peer-to-peer networking daemon with remote execution, port forwarding, autostart, self-update, and token-protected localhost API behavior.

Mitigation: Install only when those networking capabilities are intended, review the documented security controls, and keep remote execution and forwarding disabled unless peer trust and ACLs are narrowly configured.

Risk: Bearer tokens and session tokens are used for local REST and WebSocket access.

Mitigation: Use the documented Authorization header flow for durable tokens, use short-lived session tokens for browser/WebSocket query parameters, and avoid exposing the localhost API beyond the intended machine.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Publisher Profile](https://clawhub.ai/user/jimcollinson)
- [Project Repository](https://github.com/saorsa-labs/x0x)
- [Project Homepage](https://saorsalabs.com)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [macOS arm64 Binary](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 Binary](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU Binary](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU Binary](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 Binary](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, TOML configuration, and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that install binaries, start a local daemon, configure networking, call localhost APIs, manage peer trust, and control high-risk features.]

## Skill Version(s):

0.39.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
