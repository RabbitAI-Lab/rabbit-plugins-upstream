## Description:

Secure computer-to-computer networking for AI agents - gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, configure, and operate x0x for direct agent-to-agent messaging, gossip pub/sub, replicated CRDT state, encrypted groups, local daemon APIs, and trusted peer networking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and operates a local networking daemon with peer-to-peer connectivity, localhost API access, peer forwarding, and trusted-machine workflows.

Mitigation: Install only when those networking capabilities are intended, keep the API token files protected, and review daemon configuration before enabling persistent or autostart operation.

Risk: Remote execution and loopback port forwarding can run commands or expose local services on trusted peer machines if enabled and allowed.

Mitigation: Keep remote exec disabled unless required, use narrow allowlists and ACLs, require trusted contacts, and periodically review forwarding and exec diagnostics.

Risk: Self-update and installer workflows download release assets or scripts from GitHub.

Mitigation: Review installer behavior before running it, prefer verified release paths where available, and confirm upgrade settings before applying updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Publisher profile](https://clawhub.ai/user/jimcollinson)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs homepage](https://saorsalabs.com)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Release download metadata - Linux x64 GNU](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions, API calls]

**Output Format:** [Markdown with bash, JSON, TOML, and REST/WebSocket examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local daemon setup, CLI workflows, API examples, trust controls, and operational security guidance.]

## Skill Version(s):

0.39.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
