## Description:

Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use x0x to set up secure peer-to-peer networking between AI agents, including gossip broadcast, direct messaging, shared CRDT state, group encryption, file transfer, diagnostics, and optional peer connectivity features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs a persistent peer-to-peer networking daemon.

Mitigation: Start the daemon and enable autostart only when persistent networking is intended, and monitor its health and configuration.

Risk: The local API token can authorize daemon operations if exposed.

Mitigation: Keep the durable API token private, use short-lived session tokens for URL-based browser or WebSocket access, and avoid sharing token-bearing logs.

Risk: Remote command execution can run commands on a peer machine when enabled.

Mitigation: Leave remote exec disabled unless required, and enable it only with verified trusted contacts plus narrow per-peer and per-command allowlists.

Risk: Port forwarding and peer connectivity can expose loopback services to trusted peers.

Mitigation: Trust and pin peers carefully, require explicit connect ACLs, and restrict forwarding targets to intended loopback services.

Risk: Installer and self-update flows download executable code.

Mitigation: Review installers and update behavior before applying changes, and use verified release paths when installing or updating.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Publisher Profile](https://clawhub.ai/user/jimcollinson)
- [Saorsa Labs Homepage](https://saorsalabs.com)
- [x0x Repository](https://github.com/saorsa-labs/x0x)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [macOS ARM64 Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 GNU Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux ARM64 GNU Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 Download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with bash, JSON, TOML, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local daemon setup, REST/WebSocket usage, trust controls, diagnostics, forwarding, remote exec, and self-update guidance.]

## Skill Version(s):

0.40.4 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
