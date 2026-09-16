## Description:

Secure computer-to-computer networking for AI agents \u2014 gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install, start, configure, and interact with x0x peer-to-peer networking for agent messaging, group coordination, CRDT-backed task work, tailnet access, and API-based automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent networking binaries from mutable release downloads and may start or control a daemon.

Mitigation: Install only from a trusted publisher path, prefer pinned and signature-verifying downloads, and review unsigned shell installers before execution.

Risk: The daemon exposes powerful API controls protected by bearer tokens.

Mitigation: Keep the API bound to loopback unless it is behind real TLS, and protect the durable api-token like a password.

Risk: Daemon self-update and remote execution can change runtime behavior or run commands on peer machines.

Mitigation: Disable daemon self-update unless intended, and enable remote execution only with strict per-command ACLs.

## Reference(s):

- [ClawHub x0x Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x Repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [Linux x64 GNU Release Asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux ARM64 GNU Release Asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [macOS ARM64 Release Asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 Release Asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Windows x64 Release Asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include install commands, daemon configuration, REST API examples, and operational cautions for x0x.]

## Skill Version(s):

0.45.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
