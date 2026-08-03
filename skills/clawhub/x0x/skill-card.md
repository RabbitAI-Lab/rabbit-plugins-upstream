## Description: <br>
Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimcollinson](https://clawhub.ai/user/jimcollinson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use x0x to install, configure, and operate a persistent peer-to-peer networking daemon for agent messaging, CRDT-backed coordination, encrypted groups, file transfer, and trusted machine-to-machine connectivity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and operates a persistent peer-to-peer networking daemon with high-risk capabilities. <br>
Mitigation: Install it only when that daemon behavior is intended, review the release source, and keep the daemon configuration explicit. <br>
Risk: Local API tokens and identity keys can grant access to agent networking and messaging operations. <br>
Mitigation: Protect the api-token and identity key files, and keep the REST API bound to localhost unless remote exposure has been reviewed. <br>
Risk: Remote execution, port forwarding, autostart, and self-update apply paths can materially expand system exposure. <br>
Mitigation: Leave these paths disabled unless peer trust, ACL configuration, and update provenance have been reviewed. <br>


## Reference(s): <br>
- [ClawHub x0x Skill Page](https://clawhub.ai/jimcollinson/skills/x0x) <br>
- [x0x Repository](https://github.com/saorsa-labs/x0x) <br>
- [Saorsa Labs](https://saorsalabs.com) <br>
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md) <br>
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md) <br>
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md) <br>
- [Diagnostics](https://github.com/saorsa-labs/x0x/blob/main/docs/diagnostics.md) <br>
- [Remote Exec](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md) <br>
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md) <br>
- [macOS arm64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz) <br>
- [macOS x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz) <br>
- [Linux x64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz) <br>
- [Linux arm64 GNU release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz) <br>
- [Windows x64 release archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, REST examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes platform-specific install options, daemon commands, REST and WebSocket examples, and security-sensitive setup guidance.] <br>

## Skill Version(s): <br>
0.35.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
