## Description: <br>
Secure computer-to-computer networking for AI agents: gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimcollinson](https://clawhub.ai/user/jimcollinson) <br>

### License/Terms of Use: <br>
MIT OR Apache-2.0 <br>


## Use Case: <br>
Developers and agent builders use this skill to install, configure, and operate x0x for peer-to-peer agent messaging, encrypted groups, replicated task or key-value state, and local daemon APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and guides use of a local peer-to-peer networking daemon with high-impact networking features. <br>
Mitigation: Install it only when you intend to run a local P2P daemon, review release provenance before installing or upgrading, and enable autostart, port forwards, or remote execution only after reviewing peer trust and ACL settings. <br>
Risk: The daemon uses local API credentials for REST, WebSocket, and CLI workflows. <br>
Mitigation: Keep the API token private, avoid placing durable tokens in URLs, and use short-lived session tokens where the documented workflow requires browser or WebSocket access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x) <br>
- [Publisher profile](https://clawhub.ai/user/jimcollinson) <br>
- [Saorsa Labs homepage](https://saorsalabs.com) <br>
- [x0x repository](https://github.com/saorsa-labs/x0x) <br>
- [Security and cryptography documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md) <br>
- [Full API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md) <br>
- [SDK quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md) <br>
- [Symphony integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md) <br>
- [macOS arm64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz) <br>
- [macOS x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz) <br>
- [Linux x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz) <br>
- [Linux arm64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz) <br>
- [Windows x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, curl examples, configuration snippets, and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for documented download and API examples; installation metadata provides platform-specific binary download URLs.] <br>

## Skill Version(s): <br>
0.34.3 (source: evidence release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
