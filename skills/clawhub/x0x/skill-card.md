## Description:

x0x provides secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use x0x to install or connect to a local x0x daemon, establish peer-to-peer networking, exchange direct messages, broadcast gossip topics, synchronize CRDT-backed tasks, and configure encrypted groups or tailnet forwarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and update paths can place mutable or unverified executables on the user's system.

Mitigation: Prefer pinned, signature- or checksum-verified release paths, review downloaded installers before execution, and do not bypass verification failures.

Risk: The persistent local networking daemon can hold identity material, message history, bearer tokens, and local network access.

Mitigation: Keep the REST API bound to loopback, protect durable tokens, disable autostart or self-update when not needed, and start the daemon only with human authorization.

Risk: Remote execution can run unintended commands if enabled with broad permissions.

Mitigation: Enable remote execution only when required and restrict it with tight exact-argv ACLs.

Risk: Gossip pub/sub payloads are readable by relaying peers.

Mitigation: Do not publish sensitive data to gossip topics; use direct messages or MLS-encrypted groups for private communication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x Symphony integration documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [x0x signature-checking installer](https://github.com/saorsa-labs/x0x/blob/main/scripts/install.py)
- [macOS arm64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and HTTP API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes install, daemon startup, identity, messaging, group, task, and tailnet workflows; prebuilt install paths require curl and x0x/x0xd release binaries.]

## Skill Version(s):

0.45.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
