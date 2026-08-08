## Description:

Secure computer-to-computer networking for AI agents with gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to install and operate x0x as local peer-to-peer networking infrastructure for direct agent communication, group messaging, replicated task or key-value state, file transfer, diagnostics, and trusted machine-to-machine workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and documents a powerful local peer-to-peer networking daemon.

Mitigation: Install only when that infrastructure is intended, start the daemon explicitly, and review the documented configuration before use.

Risk: Local API tokens and identity keys can authorize access or represent machine, agent, and optional human identities.

Mitigation: Protect the api-token and key files and avoid exposing durable tokens in URLs or shared logs.

Risk: Remote execution and TCP port forwarding can affect peer machines if enabled broadly.

Mitigation: Enable remote exec or port forwarding only for trusted peers and keep ACLs narrow, exact, and reviewed.

Risk: Self-update and downloaded binaries change the installed networking surface.

Mitigation: Review updates before applying them and prefer the documented verification path where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Security and cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [SDK quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [OpenClaw Linux x64 install artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [OpenClaw macOS arm64 install artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [OpenClaw Windows x64 install artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, TOML, JSON, REST, WebSocket, and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes installation guidance, daemon configuration, API usage examples, and security-sensitive operational cautions.]

## Skill Version(s):

0.36.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
