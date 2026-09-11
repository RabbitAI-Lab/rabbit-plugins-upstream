## Description:

Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

External developers and agent operators use this skill to install, start, configure, and interact with x0x for peer-to-peer agent messaging, group coordination, CRDT-backed task and key-value stores, tailnet connectivity, and related owner/delegation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and can update persistent networking daemon binaries from mutable GitHub release URLs.

Mitigation: Install only when you trust Saorsa Labs' release process; prefer pinned or source-built installs and verify release signatures or checksums independently.

Risk: The x0x daemon exposes a REST API controlled by bearer tokens and can be bound beyond loopback.

Mitigation: Keep the REST API bound to loopback unless TLS and access controls are added, and protect the durable API token.

Risk: Self-update behavior can change binaries in managed environments.

Mitigation: Disable or tightly control self-update where change management is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [OpenClaw install artifact: Linux x64 GNU](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [OpenClaw install artifact: macOS ARM64](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [OpenClaw install artifact: Windows x64](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, REST examples, configuration snippets, and code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may instruct an agent to install and control persistent x0x daemon and CLI binaries.]

## Skill Version(s):

0.41.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
