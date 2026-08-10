## Description:

Secure computer-to-computer networking for AI agents -- gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

Developers and engineers use this skill to install, run, configure, and integrate x0x as a local peer-to-peer networking daemon for agent messaging, CRDT-backed collaboration, group encryption, task coordination, and trusted machine-to-machine connectivity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running x0x starts a local peer-to-peer agent networking daemon with sensitive networking features.

Mitigation: Install only when local P2P agent networking is intended, and review binary source or release trust before deployment.

Risk: The local api-token controls authenticated daemon routes and can expose messaging, group, and network operations if mishandled.

Mitigation: Protect the local api-token, use bearer headers for durable credentials, and avoid putting durable tokens in URLs.

Risk: Remote exec, autostart, self-update, and tailnet forwarding can change local system behavior or expose local services.

Mitigation: Enable these features only for peers and commands that are deliberately trusted, and review trust controls and ACLs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs homepage](https://saorsalabs.com)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [macOS arm64 release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux arm64 GNU release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Code snippets, Guidance]

**Output Format:** [Markdown with inline shell, JSON, TOML, REST, and WebSocket examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup, daemon operation, API integration, and trust-management guidance for x0x CLI and service workflows.]

## Skill Version(s):

0.37.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
